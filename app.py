import streamlit as st
import requests
import time
import random
import string

# Page Configuration
st.set_page_config(page_title="RR Username Hunter", page_icon="⚡")

st.title("⚡ Rec Room Username Hunter")

# Sidebar Settings
st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Select Mode:", ["3-Char (Random)", "4-Char (Random)", "Custom List"])
num_to_check = st.sidebar.slider("Number of users to check:", 10, 1000, 100)
delay = st.sidebar.slider("Delay between checks (seconds):", 0.1, 1.0, 0.3)

def check_user(user):
    # Added rotating user agents to look more like a browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = f"https://rec.net/user/{user}"
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 404:
            return "available"
        elif response.status_code == 200:
            return "taken"
        else:
            return "rate_limit"
    except:
        return "error"

def generate_user(length):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# Main Logic
if "Custom" in mode:
    user_input = st.text_area("Enter usernames (one per line):")
    to_check = user_input.split('\n') if user_input else []
    start_btn = st.button("Start Checking List")
else:
    length = 3 if "3" in mode else 4
    to_check = [generate_user(length) for _ in range(num_to_check)]
    start_btn = st.button(f"Generate & Check {num_to_check} Users")

if start_btn and to_check:
    st.divider()
    found_list = []
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Create columns for real-time results
    col1, col2 = st.columns(2)
    
    for idx, user in enumerate(to_check):
        user = user.strip()
        if not user: continue
        
        status_text.text(f"Checking: {user} ({idx+1}/{len(to_check)})")
        result = check_user(user)
        
        if result == "available":
            col1.success(f"Available: {user}")
            found_list.append(user)
        elif result == "rate_limit":
            st.error("Rate limit detected! Slow down the delay in settings.")
            break
        
        # Update progress
        progress_bar.progress((idx + 1) / len(to_check))
        time.sleep(delay)

    st.divider()
    if found_list:
        st.balloons()
        st.write(f"### Found {len(found_list)} Available Usernames:")
        st.code("\n".join(found_list))
    else:
        st.info("No available usernames found in this batch. Try again!")

st.caption("Performance Mode Active | Max 1000 Users")
