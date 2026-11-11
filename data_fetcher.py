import yfinance as yf
import pandas as pd

def fetch_market_data(symbol="EUR/USD"):
    symbol_map = {
        "EUR/USD": "EURUSD=X",
        "GBP/USD": "GBPUSD=X",
        "USD/JPY": "USDJPY=X",
        "AUD/USD": "AUDUSD=X",
        "USD/CAD": "USDCAD=X",
        "USD/CHF": "USDCHF=X",
        "NZD/USD": "NZDUSD=X",
        "GOLD (XAU/USD)": "GC=F",
        "SILVER (XAG/USD)": "SI=F"
    }
    
    yf_symbol = symbol_map.get(symbol, "EURUSD=X")
    
    try:
        data = yf.download(yf_symbol, period="1d", interval="1m", progress=False)
        if data.empty:
            raise ValueError("No data")
        
        df = pd.DataFrame()
        df["Time"] = data.index
        df["Price"] = data["Close"].values.flatten()
        df["Volume"] = data["Volume"].values.flatten() if "Volume" in data else 500
        return df
    except Exception:
        dates = pd.date_range(start="2026-01-01", periods=50, freq="min")
        df = pd.DataFrame({
            "Time": dates,
            "Price": [1.0850] * 50,
            "Volume": [500] * 50
        })
        return df
