import streamlit as st
import requests
import time
import random
import string

# إعدادات الصفحة
st.set_page_config(page_title="Rec Room Hunter", page_icon="🎯")

st.title("🎯 صائد يوزرات ريك روم")

# القائمة الجانبية
st.sidebar.header("الاعدادات")
mode = st.sidebar.selectbox("اختر نمط الفحص:", ["تخمين ثلاثي (3)", "تخمين رباعي (4)", "فحص قائمة مخصصة"])
num_to_check = st.sidebar.slider("عدد اليوزرات للفحص:", 5, 100, 20)

def check_user(user):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    url = f"https://rec.net/user/{user}"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 404:
            return "available"
        return "taken"
    except:
        return "error"

def generate_user(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# واجهة المستخدم الرئيسية
if "custom" in mode.lower() or "قائمة" in mode:
    user_list = st.text_area("ادخل اليوزرات (كل يوزر في سطر):")
    action_btn = st.button("بدء فحص القائمة")
    to_check = user_list.split('\n') if user_list else []
else:
    length = 3 if "3" in mode or "ثلاثي" in mode else 4
    action_btn = st.button(f"بدء تخمين {num_to_check} يوزر")
    to_check = [generate_user(length) for _ in range(num_to_check)]

if action_btn and to_check:
    st.write("---")
    found = []
    progress = st.progress(0)
    
    for idx, user in enumerate(to_check):
        user = user.strip()
        if not user: continue
        
        result = check_user(user)
        
        if result == "available":
            st.success(f"✅ متاح: {user}")
            found.append(user)
        elif result == "taken":
            st.text(f"❌ مأخوذ: {user}")
        else:
            st.warning(f"⚠️ خطأ في الاتصال: {user}")
            
        time.sleep(0.7) # حماية من الحظر
        progress.progress((idx + 1) / len(to_check))
    
    st.divider()
    if found:
        st.balloons()
        st.write("### اليوزرات المتاحة اللي لقيناها:")
        st.code("\n".join(found))
    else:
        st.error("للأسف ما لقينا شي متاح في هذي الجولة. جرب مرة ثانية!")

st.caption("Rec Room Checker v2.0 - Fixed Syntax")
