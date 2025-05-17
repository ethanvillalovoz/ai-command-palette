# AI Command Palette

AI Command Palette is a Python-based tool that accepts natural language input and performs system-level tasks. It supports commands like opening applications, summarizing text files, and sending emails.

## Features
- **Open Applications**: Launch macOS applications via natural language.
- **Summarize Text Files**: Summarize the content of `.txt` files.
- **Send Emails**: Mock email sending by printing to the console.

## Project Structure
- `main.py`: Entry point for the CLI.
- `intent_parser/`: Module for parsing user intents.
- `action_handlers/`: Module for handling specific actions.
- `ui/`: Optional Streamlit-based UI.

## Getting Started
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the CLI: `python main.py`

## Optional UI
To use the Streamlit UI, run:
```bash
streamlit run ui/app.py
```
