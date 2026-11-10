# app.py
import streamlit as st
from data_fetcher import GLOBAL_PAIRS, get_market_data
from analyzer import MarketAnalyzer
import time

st.set_page_config(
    page_title="Bot King of Pocket - التحليل الشامل",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تنسيقات CSS لتصميم النافذة العائمة والأزرار
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        height: 3em;
    }
    .main {
        direction: rtl;
    }
    /* تصميم النافذة العائمة في أسفل الشاشة */
    .floating-banner {
        position: fixed;
        bottom: 0;
        right: 0;
        left: 0;
        background-color: #1e293b;
        color: white;
        padding: 12px 20px;
        text-align: center;
        z-index: 99999;
        box-shadow: 0px -4px 10px rgba(0,0,0,0.3);
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        font-family: sans-serif;
    }
    .floating-btn {
        background-color: #2563eb;
        color: white !important;
        padding: 8px 18px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 14px;
        transition: 0.3s;
    }
    .floating-btn:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# عرض النافذة العائمة الثابتة في أسفل الشاشة لجروب التليجرام
st.markdown("""
    <div class="floating-banner">
        <span>🚀 انضم الآن إلى مجتمع التداول الرسمي على التليجرام!</span>
        <a href="https://t.me/+FoaC38eLvaBhN2I0" target="_blank" class="floating-btn">انضم الان</a>
    </div>
""", unsafe_allow_html=True)

# نظام حماية الموقع بكلمة السر
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    st.title("🔒 بوابة الدخول - Bot King of Pocket")
    st.markdown("للحصول على بوت الذكاء الاصطناعي فائق الدقة يرجى ادخال كلمة السر:")
    
    password_input = st.text_input("كلمة السر:", type="password")
    
    if st.button("دخول", type="primary"):
        if password_input == "King_Of_Pocket_BOT":
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("❌ كلمة السر غير صحيحة!")
            st.markdown(
                '📞 للحصول على كلمة السر أو الاشتراك، يرجى التواصل مع الدعم مباشرة عبر الرابط التالي: '
                '[اضغط هنا للتواصل على التيليجرام](https://t.me/king_of_pocket)',
                unsafe_allow_html=True
            )
    
    st.stop() # إيقاف عرض باقي الصفحة حتى يتم تسجيل الدخول بنجاح

# --- محتوى الموقع بعد تسجيل الدخول بنجاح ---
st.title("🤖 نظام بوت التحليل الفني وقواعد السوق المتقدمة")
st.markdown("البوت الشامل لتحليل الدعوم، المقاومات، الترندات، ومؤشرات الزخم العالمية.")

col_1, col_2 = st.columns(2)

with col_1:
    selected_key = st.selectbox(
        "اختر الزوج / الأصل:",
        options=list(GLOBAL_PAIRS.keys()),
        format_func=lambda x: GLOBAL_PAIRS[x]["name"]
    )

with col_2:
    timeframe = st.selectbox(
        "حدد الإطار الزمني للصفقة:",
        options=["1m", "5m", "15m", "30m", "1h"],
        index=0
    )

st.markdown("---")

if st.button("🚀 تحليل السوق وقواعد التداول الآن", type="primary"):
    
    with st.spinner("⏳ جاري فحص الدعوم، المقاومات، والترندات الحية للسوق..."):
        time.sleep(1.2)
        prices, pair_name = get_market_data(selected_key, interval=timeframe)
        
    if not prices:
        st.error(f"❌ حدث خطأ في جلب بيانات السوق لـ {pair_name}")
    else:
        analyzer = MarketAnalyzer(prices)
        
        rsi_result = analyzer.analyze_rsi()
        sr_result = analyzer.analyze_support_resistance()
        trend_result = analyzer.analyze_trend_and_ma()
        bb_result = analyzer.analyze_bollinger_bands()
        
        st.markdown("---")
        st.subheader(f"📊 تقرير التحليل الفني الشامل لـ [{pair_name}] ({timeframe})")
        
        st.info(f"📍 **منطقة الدعم / المقاومة:** {sr_result}")
        st.success(f"📈 **اتجاه الترند (Trend):** {trend_result}")
        st.warning(f"📉 **مؤشر القوة النسبية (RSI):** {rsi_result}")
        st.text(f"🌐 **نطاق البولنجر باند (Bollinger):** {bb_result}")
            
        st.markdown("---")
        
        results = [sr_result, trend_result, rsi_result, bb_result]
        bullish_score = sum(1 for r in results if "🟢" in r)
        bearish_score = sum(1 for r in results if "🔴" in r)
        
        if bullish_score > bearish_score and bullish_score >= 2:
            st.success(f"🟢 **الأمر النهائي: شراء / صفقة صاعدة (CALL) 🚀**\n*(توافق عدد {bullish_score} إشارات إيجابية صاعدة)*")
        elif bearish_score > bullish_score and bearish_score >= 2:
            st.error(f"🔴 **الأمر النهائي: بيع / صفقة هابطة (PUT) 🔻**\n*(توافق عدد {bearish_score} إشارات سلبية هابطة)*")
        else:
            st.warning("⏳ **الأمر النهائي: السوق متذبذب وغير واضح - يُنصح بالانتظار وعدم الدخول ⚪**")