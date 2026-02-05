import streamlit as st
import requests
import time

st.set_page_config(page_title="Rec Room Finder", page_icon="🎮")

st.title("🔍 فاحص يوزرات ريك روم")
st.write("أدخل اليوزرات اللي تبي تفحصها (يوزر واحد في كل سطر)")

# خانة إدخال اليوزرات
input_users = st.text_area("قائمة اليوزرات:", height=200, placeholder="user1\nuser2\nuser3")

if st.button("بدء الفحص"):
    if input_users:
        usernames = [u.strip() for u in input_users.split('\n') if u.strip()]
        st.info(f"جاري فحص {len(usernames)} يوزر...")
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

        for user in usernames:
            # الرابط المباشر لبروفايل اللاعب
            url = f"https://rec.net/user/{user}"
            try:
                # نرسل طلب للموقع
                response = requests.get(url, headers=headers, timeout=10)
                
                if response.status_code == 404:
                    st.success(f"✅ المتاح: {user}")
                elif response.status_code == 200:
                    st.error(f"❌ مأخوذ: {user}")
                else:
                    st.warning(f"⚠️ {user}: استجابة غير معروفة ({response.status_code})")
                
                # تأخير بسيط جداً عشان السيرفر ما يحظرك
                time.sleep(0.5)
                
            except Exception as e:
                st.error(f"خطأ في فحص {user}: {e}")
    else:
        st.warning("تكفى أدخل يوزرات أول!")

st.divider()
st.caption("ملاحظة: إذا طلع لك (
