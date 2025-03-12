import streamlit as st
import streamlit.components.v1 as components

# Configure Streamlit page
st.set_page_config(
    page_title="Network Security Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's extra margins, padding, and default UI elements
hide_streamlit_style = """
            <style>
            #MainMenu, header, footer {visibility: hidden;}
            .stDeployButton {display: none;}
            .css-18e3th9, .css-1d391kg, section.main > div {padding: 0 !important; margin: 0 !important;}
            iframe[width="0"][height="0"] {display: none;} /* Hide ghost iframes */
            .block-container {padding-top: 0px !important; padding-bottom: 0px !important; padding-left: 0px !important; padding-right: 0px !important;}
            .main {padding: 0px !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Read and embed the HTML file in full screen
with open("Network-Security-Dashboard.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1500, width=None, scrolling=True)


