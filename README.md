### README.md

# TreasureTrack

**TreasureTrack** is a Streamlit-based web application designed to forecast stock prices using the NeuralProphet model. It allows users to select from a range of popular stocks, view their historical price data, and predict future prices over a customizable number of days.

## Features

- Select from a list of well-known stocks such as Apple, Amazon, Tesla, and more.
- View historical stock data from Yahoo Finance.
- Forecast future stock prices using the NeuralProphet model.
- Interactive plot showing live stock prices and predicted future prices.
- Customizable forecast period, allowing predictions from 2 to 300 days.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- Python 3.8 or above
- Streamlit
- Pandas
- Numpy
- Plotly
- NeuralProphet
- yfinance

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/treasuretrack.git
   cd treasuretrack
   ```

2. Install the required Python packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

### How to Use

1. **Select a Stock**: Choose a stock from the dropdown list.
2. **Set Prediction Days**: Use the slider to select the number of days you want to forecast (between 2 and 300).
3. **View Historical Data**: The application will load and display the historical stock data from Yahoo Finance.
4. **Forecast Stock Prices**: The model will fit the historical data and predict future stock prices.
5. **View the Graph**: The graph will display the live data and forecasted stock prices.
6. **View the Forecasted Data**: Check the stock price predictions at the bottom of the app.

### Example Stocks Available
- Apple (AAPL)
- Tesla (TSLA)
- Microsoft (MSFT)
- Amazon (AMZN)
- Meta (META)
- NVIDIA (NVDA)
- Berkshire Hathaway (BRK.B)
- and many more...

### Project Structure

```
├── app.py              # Main Streamlit app
├── requirements.txt    # Required Python packages
└── README.md           # Project documentation
```

### License

© гเן๏ ร lคl
numpy
yfinance
neuralprophet
plotly
```
