import streamlit as st
import random
import string

# إعداد الصفحة وتغيير الثيم
st.set_page_config(page_title="Pro Email Gen", page_icon="🔴", layout="centered")

# CSS مخصص للثيم الأحمر والأسود وتوسيط العناصر
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #000000;
        color: #ffffff;
    }
    
    .main .block-container {
        max-width: 600px;
        padding-top: 3rem;
        background-color: #000000;
    }

    h1 {
        color: #ff0000;
        text-align: center;
        text-transform: uppercase;
        font-weight: 800;
        letter-spacing: 2px;
    }

    /* تنسيق الحقول */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color: #0f0f0f !important;
        color: white !important;
        border: 1px solid #440000 !important;
    }

    /* زر التوليد */
    .stButton>button {
        width: 100%;
        background-color: #ff0000;
        color: white;
        border: none;
        padding: 15px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
        margin-top: 10px;
    }
    
    .stButton>button:hover {
        background-color: #990000;
        box-shadow: 0px 0px 15px #ff0000;
        color: white;
    }

    /* صندوق النتائج */
    .stTextArea>div>div>textarea {
        background-color: #050505 !important;
        color: #ffffff !important;
        border: 1px solid #ff0000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔴 PRO EMAIL GENERATOR")

# توزيع العناصر في المنتصف
col1, col2 = st.columns(2)

with col1:
    prefix = st.text_input("First Character", "s")
    content_type = st.selectbox("Content Type", ["Alphanumeric", "Letters Only", "Numbers Only"])

with col2:
    suffix = st.text_input("Suffix Symbol", "-")
    count = st.number_input("Amount", min_value=1, max_value=10000, value=10)

middle_len = st.slider("Middle Length", 1, 25, 6)

# قائمة الدومينات مع خيار الكستم
domains_list = [
    "msn.com", "hotmail.com", "outlook.com", "live.com", 
    "yahoo.com", "gmail.com", "aol.com", "protonmail.com", "Custom Domain"
]
domain_choice = st.selectbox("Select Domain", domains_list)

if domain_choice == "Custom Domain":
    final_domain = st.text_input("Enter your custom domain (e.g. domain.com):")
else:
    final_domain = domain_choice

# زر التوليد تحت الخيارات مباشرة
if st.button("GENERATE EMAILS"):
    if not final_domain:
        st.error("Please provide a domain name!")
    else:
        results = []
        chars = string.ascii_lowercase + string.digits
        if content_type == "Letters Only": chars = string.ascii_lowercase
        elif content_type == "Numbers Only": chars = string.digits

        for _ in range(count):
            mid = ''.join(random.choice(chars) for _ in range(middle_len))
            email = f"{prefix}{mid}{suffix}@{final_domain}"
            results.append(email)
        
        st.markdown
