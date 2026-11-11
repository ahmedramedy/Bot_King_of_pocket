import streamlit as st
import pandas as pd
from data_fetcher import fetch_market_data
from analyzer import analyze_market

st.set_page_config(
    page_title="Bot King of Pocket",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden !important; display: none !important;}
    header {visibility: hidden !important; display: none !important;}
    footer {visibility: hidden !important; display: none !important;}
    [data-testid="stDecoration"] {display: none !important;}
    .viewerBadge_container__1QSob {display: none !important;}
    div[data-testid="stStatusWidget"] {visibility: hidden !important; display: none !important;}
    .stDeployButton {display: none !important;}
    button[kind="header"] {display: none !important;}
    
    /* إخفاء أي أيقونات عائمة في زوايا الشاشة نهائياً */
    iframe[src*="streamlit.io"], section[data-testid="stSidebarNav"] + div, div.myButton, [class*="viewerBadge"], [class*="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    .stApp { background-color: #0b0f19; color: #ffffff; }
    .stMetric { background-color: #111827; padding: 18px; border-radius: 12px; border: 1px solid #1f2937; }
    .login-card { background-color: #111827; padding: 30px; border-radius: 15px; border: 1px solid #1f2937; }
    div.stButton > button { background-color: #ef4444; color: white; border-radius: 8px; width: 100%; font-weight: bold; height: 45px; border: none; }
    div.stButton > button:hover { background-color: #dc2626; }
    </style>
    
    <script>
    // حذف الأيقونات العائمة وأزرار التحكم من الشاشة فوراً وبشكل مستمر
    const removeAllBadges = () => {
        const elements = document.querySelectorAll('iframe, [data-testid="stStatusWidget"], .viewerBadge_container__1QSob, .stDeployButton');
        elements.forEach(el => {
            if (el.getBoundingClientRect().bottom > window.innerHeight - 100 || el.getBoundingClientRect().right > window.innerWidth - 100) {
                el.remove();
            }
        });
        // البحث داخل الـ Shadow DOM أو الأصفار العائمة الخاصة بالمتصفح
        const allDivs = document.querySelectorAll('div');
        allDivs.forEach(div => {
            const pos = window.getComputedStyle(div).position;
            if ((pos === 'fixed' || pos === 'absolute') && div.getBoundingClientRect().bottom > window.innerHeight - 80) {
                if (!div.classList.contains('telegram-bar')) {
                    div.remove();
                }
            }
        });
    };
    setInterval(removeAllBadges, 200);
    window.addEventListener('load', removeAllBadges);
    </script>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

CORRECT_PASSWORD = "King_Of_Pocket_BOT"

if not st.session_state.authenticated:
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("""
            <div class="login-card">
                <h2 style='text-align: center; color: #ffffff; margin-bottom: 10px;'>🔐 بوابة الدخول الرقمية</h2>
                <p style='text-align: center; color: #9ca3af; font-size: 14px;'>منصة Bot King of Pocket للتحليل الفني الذكي</p>
            </div>
        """, unsafe_allow_html=True)
        
        password_input = st.text_input("أدخل كلمة المرور السرية:", type="password", placeholder="اكتب كلمة السر هنا...")
        
        if st.button("تسجيل الدخول للمنصة"):
            if password_input == CORRECT_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("كلمة المرور غير صحيحة. يرجى التأكد منها.")
                st.markdown("<div style='text-align: center;'><a href='https://t.me/+FoaC38eLvaBhN2I0' target='_blank' style='color: #60a5fa;'>الانضمام لمجتمع التليجرام للحصول على الكود</a></div>", unsafe_allow_html=True)

else:
    st.markdown("<h1 style='color: #f3f4f6;'>⚡ Bot King of Pocket | محطة التداول والتحليل الذكي</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9ca3af;'>نظام التحليل الفني اللحظي المتقدم وإدارة الصفقات بدقة عالية.</p>", unsafe_allow_html=True)
    st.markdown("---")

    all_symbols = [
        "EUR/USD", "GBP/USD", "USD/JPY", "AUD/USD", 
        "USD/CAD", "USD/CHF", "NZD/USD", 
        "EUR/GBP", "EUR/JPY", "GBP/JPY", 
        "GOLD (XAU/USD)", "SILVER (XAG/USD)",
        "BITCOIN (BTC/USD)", "ETHEREUM (ETH/USD)"
    ]
    symbol = st.selectbox("اختر أصل التداول المباشر:", all_symbols)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
    with col_b2:
        run_analysis = st.button("🔍 تحليل الآن")

    if run_analysis:
        with st.spinner("جاري جلب أسعار السوق العالمي الحية وتحليل المؤشرات الفنية..."):
            df = fetch_market_data(symbol)
            analysis = analyze_market(df)

        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(label="الأصل النشط", value=symbol, delta="سعر حقيقي مباشر")
        with col2:
            st.metric(label="السعر الحالي", value=str(analysis["price"]), delta="Live Market")
        with col3:
            st.metric(label="قوة الإشارة", value=analysis["strength"], delta="AI Model")
        with col4:
            st.metric(label="مؤشر القوة (RSI)", value=str(analysis["rsi"]), delta="14 Min")

        st.markdown("---")

        st.subheader("🎯 القرار الفني والإشارة المباشرة:")
        if "شراء" in analysis["signal"]:
            st.success(f"القرار: **{analysis['signal']}**")
        elif "بيع" in analysis["signal"]:
            st.error(f"القرار: **{analysis['signal']}**")
        else:
            st.warning(f"القرار: **{analysis['signal']}**")

        st.info(f"💡 **سبب دخول الصفقة وتحليل السعر:**\n\n{analysis['reason']}")

        st.subheader(f"📊 الشارت الفني المباشر لـ {symbol}")
        chart_df = df.set_index("Time")[["Price"]]
        st.line_chart(chart_df, color="#38bdf8")

st.markdown("""
    <style>
    .telegram-bar {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #111827;
        color: white;
        text-align: center;
        padding: 12px;
        font-size: 15px;
        font-weight: bold;
        z-index: 99999;
        border-top: 1px solid #374151;
        box-shadow: 0 -4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .telegram-bar a {
        background-color: #2563eb;
        color: white;
        padding: 6px 16px;
        border-radius: 6px;
        text-decoration: none;
        margin-right: 12px;
        font-size: 14px;
    }
    .telegram-bar a:hover {
        background-color: #1d4ed8;
    }
    </style>
    <div class="telegram-bar">
        📢 انضم الآن إلى مجتمع التليجرام الرسمي للحصول على التحديثات والإشارات الحصرية!
        <a href="https://t.me/+FoaC38eLvaBhN2I0" target="_blank">انضم الآن</a>
    </div>
""", unsafe_allow_html=True)
