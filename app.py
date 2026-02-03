import streamlit as st
import random
import string

st.title("مولد الإيميلات المخصص 📧")

# القائمة الجانبية للإعدادات
with st.sidebar:
    prefix = st.text_input("الحرف الأول", "s")
    middle_len = st.slider("عدد خانات المنتصف", 1, 15, 5)
    content_type = st.selectbox("نوع النص", ["حروف وأرقام", "حروف فقط", "أرقام فقط"])
    suffix = st.text_input("علامة الختام (مثلاً -)", "")
    
    domains_list = ["msn.com", "hotmail.com", "gmail.com", "outlook.com", "aol.com", "yahoo.com"]
    chosen_domain = st.selectbox("اختر الدومين", domains_list)
    
    count = st.number_input("الكمية", min_value=1, max_value=1000, value=10)

if st.button("توليد الإيميلات"):
    results = []
    chars = string.ascii_lowercase + string.digits
    if content_type == "حروف فقط": chars = string.ascii_lowercase
    elif content_type == "أرقام فقط": chars = string.digits

    for _ in range(count):
        mid = ''.join(random.choice(chars) for _ in range(middle_len))
        email = f"{prefix}{mid}{suffix}@{chosen_domain}"
        results.append(email)
    
    st.success(f"تم توليد {count} إيميل!")
    st.text_area("النتائج:", value="\n".join(results), height=300)