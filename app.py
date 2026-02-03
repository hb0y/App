import streamlit as st
import random
import string

# إعداد الصفحة وتغيير الثيم إلى الأسود والأحمر
st.set_page_config(page_title="Pro Email Gen", page_icon="🔴", layout="centered")

# CSS مصلح بالكامل لتوسيط الواجهة وتنسيق الأزرار
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
        padding-top: 2rem;
    }

    h1 {
        color: #ff0000;
        text-align: center;
        text-transform: uppercase;
        font-weight: 800;
        letter-spacing: 2px;
        margin-bottom: 25px;
    }

    /* تنسيق الحقول لتكون سوداء بحدود حمراء */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stNumberInput>div>div>input {
        background-color: #0f0f0f !important;
        color: white !important;
        border: 1px solid #330000 !important;
    }

    /* زر التوليد الأحمر الكبير */
    .stButton>button {
        width: 100%;
        background-color: #ff0000;
        color: white;
        border: none;
        padding: 15px;
        font-weight: bold;
        border-radius: 8px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #990000;
        box-shadow: 0px 0px 15px #ff0000;
        color: white;
    }

    /* مربع النتائج */
    .stTextArea>div>div>textarea {
        background-color: #050505 !important;
        color: #ffffff !important;
        border: 1px solid #ff0000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔴 PRO EMAIL GENERATOR")

# توزيع المدخلات في المنتصف
col1, col2 = st.columns(2)

with col1:
    prefix = st.text_input("First Character", "w")
    content_type = st.selectbox("Content Type", ["Alphanumeric", "Letters Only", "Numbers Only"])

with col2:
    suffix = st.text_input("Suffix Symbol", "-")
    count = st.number_input("Amount", min_value=1, max_value=20000, value=10)

middle_len = st.slider("Middle Length", 1, 30, 6)

# قائمة الدومينات مع خيار الـ Custom
domains_list = [
    "msn.com", "hotmail.com", "outlook.com", "live.com", 
    "yahoo.com", "gmail.com", "aol.com", "protonmail.com", "Custom Domain"
]
domain_choice = st.selectbox("Select Domain", domains_list)

# منطق الكستم دومين
if domain_choice == "Custom Domain":
    final_domain = st.text_input("Enter your custom domain (e.g., example.net):")
else:
    final_domain = domain_choice

# زر التوليد
if st.button("GENERATE EMAILS"):
    if not final_domain:
        st.error("Please enter a domain name!")
    else:
        results = []
        chars = string.ascii_lowercase + string.digits
        if content_type == "Letters Only": chars = string.ascii_lowercase
        elif content_type == "Numbers Only": chars = string.digits

        for _ in range(count):
            mid = ''.join(random.choice(chars) for _ in range(middle_len))
            email = f"{prefix}{mid}{suffix}@{final_domain}"
            results.append(email)
        
        emails_text = "\n".join(results)
        
        st.markdown("---")
        st.success(f"Generated {count} emails!")
        st.text_area("Results", value=emails_text, height=300)
        
        # زر إضافي لتحميل الملف
        st.download_button(
            label="Download as .txt",
            data=emails_text,
            file_name="generated_emails.txt",
            mime="text/plain"
        )
