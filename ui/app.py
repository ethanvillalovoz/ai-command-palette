import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import subprocess
import streamlit as st
import matplotlib.pyplot as plt
from action_handlers.summarize_file import summarize_file
from action_handlers.send_email import send_email

# Set page config
st.set_page_config(page_title="AI Command Palette", page_icon="✨", layout="wide")

# --- Custom CSS for Apple-like look and dark mode only ---
apple_css = """
<style>
body, .stApp {{
    font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
    background: #181818;
    color: #f5f5f7;
}}
h1, h2, h3, h4, h5, h6 {{
    font-weight: 600;
    letter-spacing: -0.5px;
    color: #f5f5f7;
}}
.stButton>button, .stTextInput>div>input, .stTextArea>div>textarea {{
    border-radius: 12px;
    padding: 0.75em 1.5em;
    font-size: 1.1em;
    color: #f5f5f7;
    background: #232323;
}}
.stSidebar {{
    background: #232336 !important; /* Lighter, bluish-dark for better logo contrast */
}}
.section {{
    background: #232323;
    border-radius: 18px;
    padding: 2.5em 2em;
    margin-bottom: 2em;
    box-shadow: 0 4px 24px rgba(0,0,0,0.07);
    color: #f5f5f7;
}}
.divider {{
    border-top: 1px solid #444;
    margin: 2em 0;
}}
.centered {{
    display: flex;
    flex-direction: column;
    align-items: center;
}}
/* Nav bar styling */
.navbar {{
    display: flex;
    justify-content: center;
    gap: 1.5em;
    margin: 2em 0 2.5em 0;
}}
.navbar-btn {{
    background: #232323;
    color: #f5f5f7;
    border: 2px solid #444;
    border-radius: 12px;
    padding: 0.7em 2.2em;
    font-size: 1.1em;
    font-weight: 600;
    letter-spacing: 0.5px;
    cursor: pointer;
    transition: background 0.2s, color 0.2s, border 0.2s;
}}
.navbar-btn.selected, .navbar-btn:hover {{
    background: #f5f5f7;
    color: #181818;
    border: 2px solid #f5f5f7;
}}
</style>
"""
st.markdown(apple_css, unsafe_allow_html=True)

# --- Sidebar Logo Only ---
st.sidebar.image("branding/logo2.png", use_container_width=True)

# --- Tabs for Navigation (use Streamlit's native tabs for interactivity) ---
tab_labels = ["Home", "Summarize", "Open App", "Send Email"]
tabs = st.tabs(tab_labels)

# --- Home Page ---
with tabs[0]:
    st.markdown('<div class="centered"><h1>AI Command Palette</h1></div>', unsafe_allow_html=True)
    st.markdown('<div class="centered"><h2 style="font-weight:400;">Your all-in-one AI productivity tool</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section centered">'
        '<h3>What can you do?</h3>'
        '<ul style="font-size:1.15em;">'
        '<li>Summarize and analyze documents with AI</li>'
        '<li>Open applications instantly</li>'
        '<li>Send emails with smart suggestions</li>'
        '<li>Visualize document statistics</li>'
        '</ul>'
        '</div>', unsafe_allow_html=True
    )

# --- Summarize Page ---
with tabs[1]:
    st.markdown('<div class="section centered">', unsafe_allow_html=True)
    st.markdown('<h2>Summarize a Document</h2>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a file to analyze", type=None)
    if uploaded_file is not None:
        documents_folder = os.path.join(os.getcwd(), "documents")
        os.makedirs(documents_folder, exist_ok=True)
        file_path = os.path.join(documents_folder, uploaded_file.name)
        try:
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File uploaded successfully: {uploaded_file.name}")
            result = summarize_file(file_path)
            if "error" in result:
                st.error(result["error"])
            else:
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                st.subheader("AI-Powered Analysis")
                st.text(result["summary"])
                st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
                st.subheader("Document Statistics")
                word_count = len(result["summary"].split())
                st.write(f"Word Count: {word_count}")
                sentiment_data = {"Positive": 40, "Neutral": 30, "Negative": 30}  # Mock data
                fig, ax = plt.subplots()
                ax.bar(sentiment_data.keys(), sentiment_data.values(), color=["green", "blue", "red"])
                ax.set_title("Sentiment Distribution")
                st.pyplot(fig)
        except Exception as e:
            st.error(f"An error occurred while processing the file: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Open App Page ---
with tabs[2]:
    st.markdown('<div class="section centered">', unsafe_allow_html=True)
    st.markdown('<h2>Open an Application</h2>', unsafe_allow_html=True)
    st.write("Select an application from the dropdown or enter its name manually.")
    st.write("**Note:** When typing manually, ensure the application name matches exactly as it appears on your system (e.g., 'Safari', 'Calculator').")
    common_apps = ["Calculator", "Safari", "Terminal", "TextEdit", "Notes"]
    app_name = st.selectbox("Common Applications:", options=[""] + common_apps, key="open_app_select")
    custom_app_name = st.text_input("Or enter the application name manually:", key="open_app_input")
    app_to_open = custom_app_name.strip() if custom_app_name else app_name
    if st.button("Open Application"):
        if not app_to_open:
            st.error("Please select or enter an application name.")
        else:
            try:
                if sys.platform == "darwin":
                    subprocess.run(["open", "-a", app_to_open], check=True)
                    st.success(f"Successfully opened application: {app_to_open}")
                elif sys.platform == "win32":
                    subprocess.run(["start", app_to_open], shell=True, check=True)
                    st.success(f"Successfully opened application: {app_to_open}")
                elif sys.platform == "linux":
                    subprocess.run(["xdg-open", app_to_open], check=True)
                    st.success(f"Successfully opened application: {app_to_open}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Send Email Page ---
with tabs[3]:
    st.markdown('<div class="section centered">', unsafe_allow_html=True)
    st.markdown('<h2>Send an Email</h2>', unsafe_allow_html=True)
    recipient = st.text_input("Recipient Email:", key="email_recipient")
    subject = st.text_input("Subject:", key="email_subject")
    message = st.text_area("Message:", key="email_message")
    if st.button("Send Email"):
        if not recipient or not subject or not message:
            st.error("Recipient email, subject, and message are required.")
        else:
            try:
                send_email({"to": recipient, "subject": subject, "message": message})
                st.success(f"Email sent to {recipient} successfully!")
            except Exception as e:
                st.error(f"An error occurred while sending the email: {e}")
    st.markdown('</div>', unsafe_allow_html=True)