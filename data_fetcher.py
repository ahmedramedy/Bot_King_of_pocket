import pandas as pd
import numpy as np

def fetch_market_data(symbol="EUR/USD"):
    np.random.seed(42)
    dates = pd.date_range(start="2026-01-01", periods=100, freq="min")
    base_price = 1.0850
    price_changes = np.random.normal(loc=0.0001, scale=0.0012, size=100)
    prices = base_price + np.cumsum(price_changes)
    
    df = pd.DataFrame({
        "Time": dates,
        "Price": prices,
        "Volume": np.random.randint(100, 1000, size=100)
    })
    return df
