# analyzer.py
import numpy as np

class MarketAnalyzer:
    def __init__(self, prices: list):
        self.prices = prices

    def analyze_rsi(self, period=14):
        if len(self.prices) < period + 1:
            return "بيانات غير كافية ⚪"
            
        gains, losses = [], []
        for i in range(1, len(self.prices)):
            change = self.prices[i] - self.prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
                
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            rsi = 100
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            
        if rsi < 35:
            return "تشبع بيعي (منطقة دعم قوية) 🟢"
        elif rsi > 65:
            return "تشبع شرائي (منطقة مقاومة قوية) 🔴"
        else:
            return "منطقة محايدة وسليمة ⚪"

    def analyze_support_resistance(self):
        if len(self.prices) < 30:
            return "محايد ⚪"
            
        current_price = self.prices[-1]
        recent_low = min(self.prices[-30:])
        recent_high = max(self.prices[-30:])
        
        # حساب المسافة النسبية لتحديد القرب الحقيقي من الدعوم أو المقاومات
        span = recent_high - recent_low
        if span == 0:
            return "محايد ⚪"
            
        position = (current_price - recent_low) / span
        
        if position <= 0.15:
            return "ارتداد قريبي من منطقة دعم قوية (صاعد) 🟢"
        elif position >= 0.85:
            return "ارتداد قريبي من منطقة مقاومة قوية (هابط) 🔴"
        else:
            return "السعر يتحرك في منتصف النطاق السعري ⚪"

    def analyze_trend_and_ma(self, fast=10, slow=30):
        if len(self.prices) < slow:
            return "بيانات غير كافية ⚪"
            
        sma_fast = sum(self.prices[-fast:]) / fast
        sma_slow = sum(self.prices[-slow:]) / slow
        
        if sma_fast > sma_slow:
            return "ترند صاعد إيجابي 🟢"
        elif sma_fast < sma_slow:
            return "ترند هابط سلبي 🔴"
        else:
            return "تذبذب عرضي جانبي ⚪"

    def analyze_bollinger_bands(self, period=20):
        if len(self.prices) < period:
            return "محايد ⚪"
            
        window = self.prices[-period:]
        sma = sum(window) / period
        std = np.std(window)
        
        upper_band = sma + (2 * std)
        lower_band = sma - (2 * std)
        current_price = self.prices[-1]
        
        if current_price <= lower_band:
            return "ملامسة الحد السفلي (فرصة صعود) 🟢"
        elif current_price >= upper_band:
            return "ملامسة الحد العلوي (فرصة هبوط) 🔴"
        else:
            return "داخل نطاق البولنجر الطبيعي ⚪"