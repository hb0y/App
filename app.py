import streamlit as st
import requests
import time
import random
import string

# Optimization for Speed
st.set_page_config(page_title="RR Hunter Pro", page_icon="🚀")

st.title("🚀 Rec Room Fast Hunter")
st.markdown("---")

# Sidebar Configuration
st.sidebar.header("Control Panel")
mode = st.sidebar.selectbox("Mode:", ["3-Chars (Ultra Rare)", "4-Chars (Rare)", "Custom List"])
count = st.sidebar.slider("Check Count:", 10, 1000, 500)
speed = st.sidebar.select_slider("Speed Level:", options=["Safe", "Fast", "Turbo"], value="Fast")

# Speed mapping
delay_map = {"Safe": 0.5, "Fast": 0.2, "Turbo": 0.05}
current_delay = delay_map[speed]

def check_username(user):
    # Rotating User-Agents to prevent IP blocks
    headers = {
        "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/{random.randint(500, 600)}.36"
    }
    url = f"https://rec.net/user/{user}"
    try:
        # Fast request with low timeout
        resp = requests.get(url, headers=headers, timeout=2)
        if resp.status_code == 404:
            return "AVAIL"
        elif resp.status_code == 200:
            return "TAKEN"
        return "BLOCKED"
    except:
        return "ERROR"

# Logic for Generation
if "Custom" in mode:
    raw_input = st.text_area("Paste List (One per line):")
    targets = [x.strip() for x in raw_input.split('\n') if x.strip()]
    btn_text = "Check Custom List"
else:
    length = 3 if "3" in mode else 4
    chars = string.ascii_lowercase + string.digits
    targets = [''.join(random.choice(chars) for _ in range(length)) for _ in range(count)]
    btn_text = f"Hunt {count} Usernames"

if st.button(btn_text):
    st.info(f"Starting Hunt... Mode: {mode} | Speed: {speed}")
    avail_list = []
    prog = st.progress(0)
    log = st.empty()
    
    # Using columns for better visual tracking
    res_col1, res_col2 = st.columns(2)
    
    for i, user in enumerate(targets):
        log.text(f"Scanning: {user} [{i+1}/{len(targets)}]")
        status = check_username(user)
        
        if status == "AVAIL":
            res_col1.success(f"FOUND: {user}")
            avail_list.append(user)
        elif status == "BLOCKED":
            st.warning("Rate limit reached! Switch speed to 'Safe' or wait 1 min.")
            break
            
        prog.progress((i + 1) / len(targets))
        time.sleep(current_delay)

    st.markdown("---")
    if avail_list:
        st.balloons()
        st.subheader("🎯 Results (Available):")
        st.code("\n".join(avail_list))
    else:
        st.error("No available usernames found. Try another batch!")

st.caption("Engine: Streamlit | Limit: 1000 | Lang: EN")
