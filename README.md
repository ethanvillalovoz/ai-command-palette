# AI Command Palette

![AI Command Palette Logo](branding/logo2.png)

AI Command Palette is a modern, Streamlit-based productivity tool that leverages AI to help you:
- Summarize and analyze documents
- Open applications instantly
- Send emails with smart suggestions
- Visualize document statistics

---

## Features

### 1. Summarize Documents
- Upload `.txt`, `.md`, `.json`, `.pdf`, `.docx`, `.csv`, or `.html` files.
- Uses OpenAI's GPT API for intelligent summarization, sentiment analysis, and keyword extraction.
- Visualizes document statistics (e.g., word count, sentiment distribution).

### 2. Open Applications
- Open common applications (e.g., Calculator, Safari, Terminal) or specify any app by name.
- Works cross-platform (macOS, Windows, Linux).

### 3. Send Emails
- Send emails with recipient, subject, and message fields.
- Uses secure SMTP (Gmail with App Passwords recommended).
- Credentials are loaded from a `.env` file for security.

### 4. Modern UI
- Apple-inspired dark mode UI with custom CSS.
- Sidebar with logo and clear navigation.
- Native tab navigation for a seamless experience.

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Conda (recommended) or virtualenv
- Gmail account with **App Passwords** enabled (for sending emails)
- OpenAI API key (for document summarization)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ai-command-palette
   ```

2. **Create and activate a Conda environment:**
   ```bash
   conda create --name ai_command python=3.8
   conda activate ai_command
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_gmail_app_password
   OPENAI_API_KEY=your_openai_api_key
   ```

   - Use a Gmail App Password, not your main password.
   - Get your OpenAI API key from https://platform.openai.com/api-keys

5. **Ensure the `.env` file is ignored by Git:**
   - The `.env` file is already listed in `.gitignore`.

---

## Running the Application

1. **Activate your environment:**
   ```bash
   conda activate ai_command
   ```

2. **Start the Streamlit app:**
   ```bash
   streamlit run ui/app.py
   ```

3. **Open the app in your browser:**
   - Go to [http://localhost:8501](http://localhost:8501)

---

## Project Structure

```
ai-command-palette/
├── action_handlers/
│   ├── summarize_file.py
│   ├── send_email.py
│   └── __init__.py
├── branding/
│   ├── logo2.png
│   └── (other images)
├── documents/
│   └── (uploaded files)
├── intent_parser/
│   └── __init__.py
├── requirements.txt
├── .env
├── .gitignore
├── ui/
│   └── app.py
└── README.md
```

---

## Troubleshooting

- **SMTP Authentication Error:**  
  Ensure you are using a Gmail App Password and the correct credentials in `.env`.

- **OpenAI API Errors:**  
  Make sure your OpenAI API key is valid and has sufficient quota.

- **File Upload Issues:**  
  Only supported file types can be summarized. For PDFs, ensure they contain extractable text.

- **Logo Visibility:**  
  The sidebar background is set for optimal logo contrast. If you use a different logo, adjust the CSS in `app.py`.

---

## Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.

---

## License

This project is licensed under the MIT License.
