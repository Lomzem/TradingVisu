import pandas as pd
import numpy as np


def get_calculations(df: pd.DataFrame):
    df = df[["T/D", "Side", "Symbol", "Qty", "Price", "Exec Time"]]
    df.rename({"T/D": "Date", "Exec Time": "Time"}, axis="columns", inplace=True)
    df.rename({"T/D": "Date"}, axis="columns", inplace=True)
    df = df.astype(
        {
            "Date": "datetime64[ns]",
            "Side": "category",
            "Qty": "float32",
            "Price": "float32",
        }
    )

    df.Qty = np.where(df.Side.isin(["SS", "S"]), -df.Qty, df.Qty)

    df["Weighted_Price"] = df.Qty * df.Price
    df["AvgPrice"] = df.groupby(
        ["Symbol", "Date", "Side"], observed=True
    ).Weighted_Price.transform("sum") / df.groupby(
        ["Symbol", "Date", "Side"], observed=True
    ).Qty.transform("sum")

    df["Qty"] = df.groupby(["Symbol", "Date", "Side"], observed=True).Qty.transform(
        "sum"
    )
    df = (
        df.groupby(["Symbol", "Date", "Side"], observed=True)
        .first()
        .reset_index()
        .dropna()
        .drop(["Price", "Weighted_Price"], axis=1)
        .sort_values(["Date", "Symbol", "Time"])
    )

    df["PriceIn"] = df.groupby(["Symbol", "Date"]).AvgPrice.transform("first")
    df["PriceOut"] = df.groupby(["Symbol", "Date"]).AvgPrice.transform("last")
    df = df.groupby(["Symbol", "Date"]).first()
    df = df.drop(["AvgPrice"], axis=1)
    df.Qty = df.Qty.abs()

    df["Gain%"] = np.where(
        df.Side.eq("SS"), -df.PriceOut / df.PriceIn + 1, df.PriceOut / df.PriceIn - 1
    )
    df["Gain$"] = np.where(
        df.Side.eq("SS"),
        (df.PriceIn - df.PriceOut) * df.Qty,
        (df.PriceOut - df.PriceIn) * df.Qty,
    )
    df["Win"] = df["Gain$"].gt(0)
    df = df.reset_index()
    df["Weekday"] = df["Date"].dt.day_name()

    max_gainp = df["Gain%"].max() * 100
    max_lossp = df["Gain%"].min() * 100
    winrate = df["Win"].mean() * 100
    max_gaind = df["Gain$"].max()
    max_lossd = df["Gain$"].min()

    weekday_perf = df.groupby("Weekday", observed=False)["Gain%"].sum().reset_index()
    best_weekday = weekday_perf.loc[weekday_perf["Gain%"].idxmax()]["Weekday"]
    worst_weekday = weekday_perf.loc[weekday_perf["Gain%"].idxmin()]["Weekday"]

    net_dgain = df["Gain$"].sum()

    profit_factor_gb = (
        df.groupby("Win", observed=False)["Gain%"].transform("sum").drop_duplicates()
    )
    profit_factor = abs(profit_factor_gb.max() / profit_factor_gb.min())

    return {
        "max_gainp": f"{max_gainp:.3g}%",
        "max_lossp": f"{max_lossp:.3g}%",
        "winrate": f"{winrate:.3g}%",
        "max_gaind": f"${max_gaind:.2f}",
        "max_lossd": f"-${abs(max_lossd):.2f}",
        "best_weekday": best_weekday,
        "worst_weekday": worst_weekday,
        "net_dgain": f"${net_dgain:.2f}",
        "profit_factor": f"{profit_factor:.3g}",
    }

    # print(f"{max_gainp:.3g}%")
    # print(f"{max_lossp:.3g}%")
    # print(f"{winrate:.3g}%")
    # print(f"${max_gaind:.2f}")
    # print(f"-${abs(max_lossd):.2f}")
    # print(best_weekday)
    # print(worst_weekday)
    # print(f"${net_dgain:.2f}")
    # print(f"{profit_factor:.3g}")
