import pandas as pd 
import numpy as np
import streamlit as st
from neuralprophet import NeuralProphet
import yfinance as yf
from plotly import graph_objs as og


st.title("TreasureTrackـــــــــــــــﮩ٨ـ")


stocks = (
    "Apple",       # AAPL
    "Alphabet",    # GOOG
    "Microsoft",   # MSFT
    "GameStop",    # GME
    "Amazon",      # AMZN
    "Tesla",       # TSLA
    "Meta",        # META
    "Berkshire Hathaway", # BRK.B
    "NVIDIA",      # NVDA
    "Visa",        # V
    "Johnson & Johnson", # JNJ
    "Walmart",     # WMT
    "Procter & Gamble", # PG
    "JPMorgan Chase", # JPM
    "UnitedHealth Group", # UNH
    "Mastercard",  # MA
    "Home Depot",  # HD
    "Pfizer",      # PFE
    "Bank of America", # BAC
    "Coca-Cola",   # KO
    "Intel",       # INTC
    "Walt Disney", # DIS
    "Verizon",     # VZ
    "Chevron",     # CVX
    "PepsiCo",     # PEP
    "AbbVie",      # ABBV
    "Salesforce",  # CRM
    "Comcast",     # CMCSA
    "Netflix",     # NFLX
    "Oracle",      # ORCL
    "IBM",         # IBM
    "3M",          # MMM
    "Qualcomm",    # QCOM
    "Texas Instruments", # TXN
    "Lilly",       # LLY
    "Morgan Stanley", # MS
    "Goldman Sachs", # GS
    "Adobe",       # ADBE
    "Amgen",       # AMGN
    "Cisco Systems", # CSCO
    "Accenture",   # ACN
    "Bristol-Myers Squibb", # BMY
    "Honeywell",   # HON
    "American Express", # AXP
    "United Parcel Service", # UPS
    "Union Pacific", # UNP
    "Charter Communications", # CHTR
    "Intuit",      # INTU
    "S&P Global",  # SPGI
    "Lockheed Martin", # LMT
    "Caterpillar",  # CAT
    "Linde",       # LIN
    "Raytheon Technologies", # RTX
    "Biogen",      # BIIB
    "Stryker",     # SYK
    "Moderna",     # MRNA
    "Kraft Heinz", # KHC
)

stocks_dict = {
    "Apple": "AAPL",
    "Alphabet": "GOOG",
    "Microsoft": "MSFT",
    "GameStop": "GME",
    "Amazon": "AMZN",
    "Tesla": "TSLA",
    "Meta": "META",
    "Berkshire Hathaway": "BRK.B",
    "NVIDIA": "NVDA",
    "Visa": "V",
    "Johnson & Johnson": "JNJ",
    "Walmart": "WMT",
    "Procter & Gamble": "PG",
    "JPMorgan Chase": "JPM",
    "UnitedHealth Group": "UNH",
    "Mastercard": "MA",
    "Home Depot": "HD",
    "Pfizer": "PFE",
    "Bank of America": "BAC",
    "Coca-Cola": "KO",
    "Intel": "INTC",
    "Walt Disney": "DIS",
    "Verizon": "VZ",
    "Chevron": "CVX",
    "PepsiCo": "PEP",
    "AbbVie": "ABBV",
    "Salesforce": "CRM",
    "Comcast": "CMCSA",
    "Netflix": "NFLX",
    "Oracle": "ORCL",
    "IBM": "IBM",
    "3M": "MMM",
    "Qualcomm": "QCOM",
    "Texas Instruments": "TXN",
    "Lilly": "LLY",
    "Morgan Stanley": "MS",
    "Goldman Sachs": "GS",
    "Adobe": "ADBE",
    "Amgen": "AMGN",
    "Cisco Systems": "CSCO",
    "Accenture": "ACN",
    "Bristol-Myers Squibb": "BMY",
    "Honeywell": "HON",
    "American Express": "AXP",
    "United Parcel Service": "UPS",
    "Union Pacific": "UNP",
    "Charter Communications": "CHTR",
    "Intuit": "INTU",
    "S&P Global": "SPGI",
    "Lockheed Martin": "LMT",
    "Caterpillar": "CAT",
    "Linde": "LIN",
    "Raytheon Technologies": "RTX",
    "Biogen": "BIIB",
    "Stryker": "SYK",
    "Moderna": "MRNA",
    "Kraft Heinz": "KHC",
}



selected_stocks=st.selectbox('Select Stocks',stocks)

n_days=st.slider("Prediction timeframe",2,300)

@st.cache_data
def load_data(stk):
    GetFacebookInformation = yf.Ticker(stk)
    stock=pd.DataFrame(GetFacebookInformation.history(period="max"))
    stock.index=pd.to_datetime(stock.index)
    stock=stock.reset_index()
    
    return stock


data=load_data(stocks_dict[selected_stocks])


st.subheader("Stock History")
st.write(data.tail())

data.rename(columns={'Date': 'ds', 'Close': 'y'}, inplace=True)
data = data[["ds", "y"]]

data_loading=st.text("Loading...")
model = NeuralProphet()
model.fit(data)
data_loading.text("Loading done...")

future = model.make_future_dataframe(data, periods=n_days)
forecast = model.predict(future)


def plot_raw_data(dt,fo):
    fig=og.Figure()
    fig.add_trace(og.Scatter(x=dt["ds"],y=dt["y"],name="Live"))
    fig.add_trace(og.Scatter(x=fo["ds"],y=fo["yhat1"],name="Calc"))
   
    fig.layout.update(title_text="Stocks",xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data(data,forecast)


forecast_to_display = forecast.drop("y", axis=1).rename(columns={'ds': 'Date', 'yhat1': 'Close'})
st.subheader("Stock Projection")
st.write(forecast_to_display.tail())
st.markdown(
    """
    © гเן๏ ร lคl
    """
)
