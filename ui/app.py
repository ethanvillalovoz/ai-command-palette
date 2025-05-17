# Streamlit UI for AI Command Palette
import sys
import os
import subprocess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from action_handlers.summarize_file import summarize_file

# Sidebar for navigation
st.sidebar.title("AI Command Palette")
page = st.sidebar.radio("Choose a command:", ["Home", "Summarize", "Open App"])

# Home Page
if page == "Home":
    st.title("Welcome to AI Command Palette!")
    st.write("""
        This application allows you to perform various commands such as:
        - Summarizing documents
        - Opening applications
        - And more!
        
        Use the sidebar to navigate between commands.
    """)
    st.image("https://via.placeholder.com/800x300.png?text=AI+Command+Palette", caption="AI Command Palette")

# Summarize Page
elif page == "Summarize":
    st.title("Summarize a Document")
    uploaded_file = st.file_uploader("Upload a file to summarize", type=None)  # Allow all file types
    
    if uploaded_file is not None:
        # Save the uploaded file to the documents folder
        documents_folder = os.path.join(os.getcwd(), "documents")
        os.makedirs(documents_folder, exist_ok=True)
        file_path = os.path.join(documents_folder, uploaded_file.name)
        
        try:
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success(f"File uploaded successfully: {uploaded_file.name}")
            
            # Summarize the uploaded file
            summary = summarize_file(file_path)
            st.subheader("Summary:")
            st.text(summary)
        except Exception as e:
            st.error(f"An error occurred while saving the file: {e}")

# Open App Page
elif page == "Open App":
    st.title("Open an Application")
    st.write("Select an application from the dropdown or enter its name manually.")
    st.write("**Note:** When typing manually, ensure the application name matches exactly as it appears on your system (e.g., 'Safari', 'Calculator').")

    # Dropdown for common applications
    common_apps = ["Calculator", "Safari", "Terminal", "TextEdit", "Notes"]
    app_name = st.selectbox("Common Applications:", options=[""] + common_apps)
    custom_app_name = st.text_input("Or enter the application name manually:")

    # Determine the application name to use
    app_to_open = custom_app_name.strip() if custom_app_name else app_name

    if st.button("Open Application"):
        if not app_to_open:
            st.error("Please select or enter an application name.")
        else:
            try:
                if sys.platform == "darwin":  # macOS
                    # Ensure the application name is passed correctly
                    result = subprocess.run(["open", "-a", app_to_open], check=True, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        st.success(f"Successfully opened application: {app_to_open}")
                    else:
                        st.error(f"Unable to open application: {app_to_open}.")
                elif sys.platform == "win32":  # Windows
                    subprocess.run(["start", app_to_open], shell=True, check=True)
                    st.success(f"Successfully opened application: {app_to_open}")
                elif sys.platform == "linux":  # Linux
                    subprocess.run(["xdg-open", app_to_open], check=True)
                    st.success(f"Successfully opened application: {app_to_open}")
            except subprocess.CalledProcessError as e:
                st.error(f"Unable to find or open application: {app_to_open}. Ensure the name is correct.")
                st.error(f"Error details: {e.stderr.strip()}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")