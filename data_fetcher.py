# data_fetcher.py
import requests

GLOBAL_PAIRS = {
    "1": {"name": "EUR/USD", "ticker": "EURUSD=X"},
    "2": {"name": "GBP/USD", "ticker": "GBPUSD=X"},
    "3": {"name": "USD/JPY", "ticker": "USDJPY=X"},
    "4": {"name": "AUD/USD", "ticker": "AUDUSD=X"},
    "5": {"name": "USD/CAD", "ticker": "USDCAD=X"},
    "6": {"name": "AUD/JPY", "ticker": "AUDJPY=X"},
    "7": {"name": "AUD/CAD", "ticker": "AUDCAD=X"},
    "8": {"name": "AUD/CHF", "ticker": "AUDCHF=X"},
    "9": {"name": "AUD/NZD", "ticker": "AUDNZD=X"},
    "10": {"name": "CAD/CHF", "ticker": "CADCHF=X"},
    "11": {"name": "CAD/JPY", "ticker": "CADJPY=X"},
    "12": {"name": "CHF/JPY", "ticker": "CHFJPY=X"},
    "13": {"name": "CHF/SGD", "ticker": "CHFSGD=X"},
    "14": {"name": "EUR/AUD", "ticker": "EURAUD=X"},
    "15": {"name": "EUR/CAD", "ticker": "EURCAD=X"},
    "16": {"name": "EUR/CHF", "ticker": "EURCHF=X"},
    "17": {"name": "EUR/GBP", "ticker": "EURGBP=X"},
    "18": {"name": "EUR/HUF", "ticker": "EURHUF=X"},
    "19": {"name": "EUR/JPY", "ticker": "EURJPY=X"},
    "20": {"name": "EUR/NZD", "ticker": "EURNZD=X"},
    "21": {"name": "EUR/PLN", "ticker": "EURPLN=X"},
    "22": {"name": "EUR/SGD", "ticker": "EURSGD=X"},
    "23": {"name": "EUR/TRY", "ticker": "EURTRY=X"},
    "24": {"name": "GBP/AUD", "ticker": "GBPAUD=X"},
    "25": {"name": "GBP/CAD", "ticker": "GBPCAD=X"},
    "26": {"name": "GBP/CHF", "ticker": "GBPCHF=X"},
    "27": {"name": "GBP/JPY", "ticker": "GBPJPY=X"},
    "28": {"name": "GOLD (الذهب)", "ticker": "GC=F"},
    "29": {"name": "SILVER (الفضة)", "ticker": "SI=F"},
    "30": {"name": "BITCOIN (البتكوين)", "ticker": "BTC-USD"},
    "31": {"name": "ETHEREUM (الإيثريوم)", "ticker": "ETH-USD"},
    "32": {"name": "RIPPLE (الريبل)", "ticker": "XRP-USD"}
}

def get_market_data(choice, interval="5m"):
    if choice not in GLOBAL_PAIRS:
        return None, "الخيار غير صحيح"
    
    pair_info = GLOBAL_PAIRS[choice]
    ticker = pair_info["ticker"]
    
    # زيادة نطاق البيانات إلى 5 أيام لضمان تنوع الشموع وإعطاء نتائج واقعية
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval={interval}&range=5d"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        result = data['chart']['result'][0]
        closes = result['indicators']['quote'][0]['close']
        
        prices = [p for p in closes if p is not None]
        
        if len(prices) < 30:
            return None, "لا توجد بيانات كافية لهذا الزوج حالياً."
            
        return prices, pair_info["name"]
    except Exception as e:
        return None, str(e)