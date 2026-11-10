# main.py
from data_fetcher import GLOBAL_PAIRS, get_market_data
from analyzer import MarketAnalyzer

def main():
    print("========================================")
    print("   🤖 نظام بوت التحليل الذكي للسوق العالمي 🤖")
    print("========================================")
    
    print("\nاختر زوج العملات أو الأصل العالمي للتحليل:")
    for key, data in GLOBAL_PAIRS.items():
        print(f"[{key}] {data['name']}")
        
    choice = input("\nأدخل رقم الزوج المطلوب: ").strip()
    
    if choice not in GLOBAL_PAIRS:
        print("❌ اختيار غير صحيح، يرجى إعادة تشغيل البوت.")
        return

    print(f"\n[+] جاري الاتصال بالسوق العالمي وجلب بيانات {GLOBAL_PAIRS[choice]['name']}...")
    prices, pair_name = get_market_data(choice)
    
    if not prices:
        print(f"❌ حدث خطأ في جلب البيانات: {pair_name}")
        return

    analyzer = MarketAnalyzer(prices)
    
    # تطبيق قواعد التحليل
    rsi_signal = analyzer.analyze_rsi()
    ma_signal = analyzer.analyze_ma_crossover()
    
    print(f"\n--- 📊 تقرير التحليل الفني لـ [{pair_name}] ---")
    print(f"1. إشارة مؤشر RSI (14): {rsi_signal}")
    print(f"2. إشارة تقاطع المتوسطات: {ma_signal}")
    print("----------------------------------------")
    
    # اتخاذ القرار النهائي
    if "صاعد" in rsi_signal and "صاعد" in ma_signal:
        print("🚀 **القرار النهائي للمشغل: صفقة صاعدة (CALL)** 🟢")
    elif "هابط" in rsi_signal and "هابط" in ma_signal:
        print("🔻 **القرار النهائي للمشغل: صفقة هابطة (PUT)** 🔴")
    else:
        print("⏳ **القرار النهائي: الانتظار وعدم الدخول (السوق غير مستقر)** ⚪")

if __name__ == "__main__":
    main()