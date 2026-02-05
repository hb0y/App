import requests
import time

def check_recroom_username(username):
    # رابط البروفايل العام في ريك روم
    url = f"https://rec.net/user/{username}"
    
    try:
        response = requests.get(url, timeout=5)
        
        # إذا كانت الصفحة تعطي 404، غالباً اليوزر متاح
        if response.status_code == 404:
            print(f"[✅ متاح] : {username}")
            return True
        else:
            print(f"[❌ مأخوذ] : {username}")
            return False
            
    except Exception as e:
        print(f"حدث خطأ أثناء الفحص: {e}")
        return None

# قائمة تجريبية لليوزرات اللي تبي تفحصها
usernames_to_check = ["super_hero", "x_99_z", "unique_name_2026"]

print("--- بدء عملية الفحص ---")
for user in usernames_to_check:
    check_recroom_username(user)
    time.sleep(1)  # تأخير بسيط عشان ما يحظرون الـ IP حقك
