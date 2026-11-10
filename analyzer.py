import pandas as pd
import numpy as np

def analyze_market(df):
    df['SMA_20'] = df['Price'].rolling(window=20).mean()
    df['SMA_50'] = df['Price'].rolling(window=50).mean()
    
    delta = df['Price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    latest_price = df['Price'].iloc[-1]
    latest_sma = df['SMA_20'].iloc[-1] if not pd.isna(df['SMA_20'].iloc[-1]) else latest_price
    latest_rsi = df['RSI'].iloc[-1] if not pd.isna(df['RSI'].iloc[-1]) else 50.0
    
    if latest_price > latest_sma and latest_rsi < 70:
        signal = "شراء (CALL) 🟢"
        strength = "94% - قوية جداً"
    elif latest_price < latest_sma and latest_rsi > 30:
        signal = "بيع (PUT) 🔴"
        strength = "91% - قوية جداً"
    else:
        signal = "انتظار / تذبذب ⏳"
        strength = "50% - محايد"
        
    return {
        "signal": signal,
        "strength": strength,
        "rsi": round(latest_rsi, 2),
        "price": round(latest_price, 5)
    }
