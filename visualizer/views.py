from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from . import df_calculations


def upload(request):
    return render(request, "upload.html")


def upload_csv(request):
    if request.method == "POST" and request.FILES["csv_file"]:
        csv_file = request.FILES["csv_file"]
        df = pd.read_csv(csv_file)

        # filename = f"temp_{csv_file.name}"
        # with open(filename, "wb+") as dst:
        #     for chunk in csv_file.chunks():
        #         dst.write(chunk)
        #
        # df = pd.read_csv(filename)

        calculations = df_calculations.get_calculations(df)

        return render(request, "visualization.html", calculations)


# def visualization(request):
#     df = pd.read_csv("temp_DailyInfo20241027015916.csv")
#     calculations = df_calculations.get_calculations(df)
#     return render(request, "visualization.html", calculations)
