# AI Command Palette

AI Command Palette is a Streamlit-based application that allows users to perform various commands, including:
- Summarizing documents
- Opening applications
- Sending emails

## Features
1. **Summarize Documents**:
   - Upload `.txt`, `.md`, `.json`, `.pdf`, `.docx`, `.csv`, or `.html` files to generate a summary.
2. **Open Applications**:
   - Open common applications like `Calculator`, `Safari`, or `Terminal` directly from the app.
3. **Send Emails**:
   - Send emails with a recipient, subject, and message using Gmail's SMTP server.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Gmail account with **App Passwords** enabled (if using Gmail for sending emails)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-command-palette
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory:
   ```plaintext
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

   - Replace `your_email@gmail.com` with your Gmail address.
   - Replace `your_app_password` with the App Password generated in your Google account.

4. Ensure the `.env` file is ignored by Git:
   - The `.env` file is already listed in `.gitignore`.

---

### Running the Application
1. Start the Streamlit app:
   ```bash
   streamlit run ui/app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

---

### Features in Detail

#### 1. Summarize Documents
- Navigate to the "Summarize" tab.
- Upload a file to generate a summary.
- Supported file types: `.txt`, `.md`, `.json`, `.pdf`, `.docx`, `.csv`, `.html`.

#### 2. Open Applications
- Navigate to the "Open App" tab.
- Select an application from the dropdown or enter its name manually.
- Click "Open Application" to launch the app.

#### 3. Send Emails
- Navigate to the "Send Email" tab.
- Enter the recipient's email, subject, and message.
- Click "Send Email" to send the email.

---

### Troubleshooting

#### Common Issues
1. **SMTP Authentication Error**:
   - Ensure you are using an App Password for Gmail.
   - Verify the credentials in the `.env` file.

2. **Environment Variables Not Loaded**:
   - Ensure the `python-dotenv` library is installed.
   - Restart the application after updating the `.env` file.

3. **File Upload Issues**:
   - Ensure the uploaded file is in a supported format.

---

### Contributing
Feel free to submit issues or pull requests to improve the project.

---

### License
This project is licensed under the MIT License.
