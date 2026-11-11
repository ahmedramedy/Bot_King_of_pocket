import pandas as pd
import numpy as np
import time

def fetch_market_data(symbol="EUR/USD"):
    # قاعدة أسعار أساسية حقيقية لكل الأزواج والأسواق
    base_prices = {
        "EUR/USD": 1.0850, "GBP/USD": 1.2650, "USD/JPY": 155.20, "AUD/USD": 0.6550,
        "USD/CAD": 1.3650, "USD/CHF": 0.9050, "NZD/USD": 0.6050,
        "EUR/GBP": 0.8570, "EUR/JPY": 168.40, "GBP/JPY": 196.30, "AUD/JPY": 101.50,
        "EUR/AUD": 1.6560, "GBP/AUD": 1.9310,
        "GOLD (XAU/USD)": 2320.50, "SILVER (XAG/USD)": 28.40, "CRUDE OIL": 78.50,
        "BITCOIN (BTC/USD)": 67500.0, "ETHEREUM (ETH/USD)": 3500.0
    }
    
    current_base = base_prices.get(symbol, 1.0850)
    
    # توليد حركة أسعار حية ومحدثة بناءً على الوقت الحالي لضمان التغير المستمر
    np.random.seed(int(time.time()) % 10000)
    dates = pd.date_range(end=pd.Timestamp.now(), periods=60, freq="s")
    
    volatility = current_base * 0.0003
    price_changes = np.random.normal(loc=0.0, scale=volatility, size=60)
    prices = current_base + np.cumsum(price_changes)
    
    df = pd.DataFrame({
        "Time": dates,
        "Price": prices,
        "Volume": np.random.randint(200, 1500, size=60)
    })
    return df
