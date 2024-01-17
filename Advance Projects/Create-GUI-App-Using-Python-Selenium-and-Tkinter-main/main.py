import streamlit as st
from selenium import webdriver

# Define the URLs for different apps
app_urls = {
    "Google": "https://www.google.com/",
    "Instagram": "https://www.instagram.com/",
    "YouTube": "https://www.youtube.com/",
    "Facebook": "https://www.facebook.com/",
    "LinkedIn": "https://www.linkedin.com/",
}

st.title("Accessing Apps through Streamlit")


# Define icons for each app
icons = {
    "Google": "🔍",
    "Instagram": "📷",
    "YouTube": "🎥",
    "Facebook": "👤",
    "LinkedIn": "🌐",
}

# Create buttons for each app with icons
selected_app = st.selectbox("Select an App", list(app_urls.keys()))
if st.button(f"{icons[selected_app]} {selected_app}"):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get(app_urls[selected_app])

selected_app = st.selectbox("Select an App", list(app_urls.keys()))
if st.button(f"{icons[selected_app]} {selected_app}"):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get(app_urls[selected_app])

selected_app = st.selectbox("Select an App", list(app_urls.keys()))
if st.button(f"{icons[selected_app]} {selected_app}"):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get(app_urls[selected_app])

selected_app = st.selectbox("Select an App", list(app_urls.keys()))
if st.button(f"{icons[selected_app]} {selected_app}"):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get(app_urls[selected_app])

selected_app = st.selectbox("Select an App", list(app_urls.keys()))
if st.button(f"{icons[selected_app]} {selected_app}"):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=option)
    driver.get(app_urls[selected_app])
