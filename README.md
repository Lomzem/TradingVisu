# TradingVisu
A trading performance calculator for TradeZero

![Screenshot of calculations](screenshot.png) 

## Statistics Displayed
The app provides users with the following statistics based on their trading data:
- Biggest Percent Win%
- Biggest Percent Loss%
- Win Rate
- Biggest Dollar Win
- Biggest Dollar Loss
- Net Dollar Gain
- Best Weekday
- Worst Weekday
- Profit Factor

<!-- - **CSV Data Upload**: Users can upload their trading data in CSV format. -->
<!-- - **Data Processing**: The app uses the Pandas library to process the uploaded data. -->
<!-- - **Dynamic HTML Generation**: Displays HTML output that includes statistics such as Win Rate and Net Gain -->

## Installation

To set up the Trading Visualizer web app, follow these steps:

1. **Clone the repository**:
```bash
git clone https://github.com/Lomzem/TradingVisu.git
cd TradingVisu
```

2. **Create a virtual environment** (optional):
```bash
python -m venv venv
source venv/bin/activate
```

3. **Install required packages**:
```bash
pip install -r requirements.txt
```

4. **Run the development server**:
```bash
python manage.py runserver
```

## Usage
1. **Access the app**: Open your web browser and navigate to `http://127.0.0.1:8000/`
2. **Upload CSV File**: Click on the **upload** button on the page and select your CSV file containing trading data.
3. **View Statistics**: The page will change into a dashboard displays statistics based on your trading data.

## Obtaining a CSV file

## Technologies Used
- **Django**: Backend framework for building the web application.
- **Pandas**: Library for data manipulation and analysis.
- **Tailwind CSS**: CSS Framework for styling the frontend


<!-- # Run the App -->
<!-- This app uses Django -->
