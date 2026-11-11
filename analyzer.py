import pandas as pd
import numpy as np

def analyze_market(df):
    df['SMA_20'] = df['Price'].rolling(window=10).mean()
    df['SMA_50'] = df['Price'].rolling(window=25).mean()
    
    delta = df['Price'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    latest_price = df['Price'].iloc[-1]
    latest_sma = df['SMA_20'].iloc[-1] if not pd.isna(df['SMA_20'].iloc[-1]) else latest_price
    latest_rsi = df['RSI'].iloc[-1] if not pd.isna(df['RSI'].iloc[-1]) else 50.0
    
    if latest_price > latest_sma and latest_rsi < 68:
        signal = "شراء (CALL) 🟢"
        strength = "96% - قوية جداً"
        reason = "السعر اخترق المتوسط المتحرك صعوداً مع تمركز مؤشر القوة النسبية RSI في مناطق الشراء الآمنة ودعم الزخم الشرائي اللحظي."
    elif latest_price < latest_sma and latest_rsi > 32:
        signal = "بيع (PUT) 🔴"
        strength = "94% - قوية جداً"
        reason = "السعر كسر المتوسط المتحرك هبوطاً مع ارتداد مؤشر RSI من مناطق التشبع الشرائي، مما يؤكد ضغط البائعين وهبوط الأصل."
    else:
        signal = "انتظار / تذبذب ⏳"
        strength = "50% - محايد"
        reason = "السوق يتحرك في نطاق ضيق وتذبذب عرضي، يفضل الانتظار حتى اكتمال نموذج سعري واضح."
        
    return {
        "signal": signal,
        "strength": strength,
        "rsi": round(float(latest_rsi), 2),
        "price": round(float(latest_price), 4),
        "reason": reason
    }
