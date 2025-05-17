import os
import json
import csv
from bs4 import BeautifulSoup  # For HTML parsing
from PyPDF2 import PdfReader  # For PDF parsing
from docx import Document  # For Word documents

def summarize_file(file_path):
    """Process a file and provide a summary or relevant output based on its type."""
    try:
        if not os.path.isfile(file_path):
            return f"File not found: {file_path}"

        _, file_extension = os.path.splitext(file_path)

        if file_extension == ".txt":
            with open(file_path, 'r') as file:
                content = file.read()
                summary = content[:200]  # Mock summary: first 200 characters
                return f"Summary of {file_path}:\n{summary}"
        elif file_extension == ".md":
            with open(file_path, 'r') as file:
                content = file.read()
                summary = content[:200]  # Mock summary for Markdown
                return f"Markdown Summary of {file_path}:\n{summary}"
        elif file_extension == ".json":
            with open(file_path, 'r') as file:
                content = json.load(file)
                summary = json.dumps(content, indent=2)[:200]  # Mock summary for JSON
                return f"JSON Summary of {file_path}:\n{summary}"
        elif file_extension == ".pdf":
            reader = PdfReader(file_path)
            content = " ".join(page.extract_text() for page in reader.pages)
            summary = content[:200]  # Mock summary for PDF
            return f"PDF Summary of {file_path}:\n{summary}"
        elif file_extension == ".docx":
            doc = Document(file_path)
            content = " ".join(paragraph.text for paragraph in doc.paragraphs)
            summary = content[:200]  # Mock summary for Word documents
            return f"Word Document Summary of {file_path}:\n{summary}"
        elif file_extension == ".csv":
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)
                summary = f"CSV contains {len(rows)} rows and {len(rows[0]) if rows else 0} columns."
                return f"CSV Summary of {file_path}:\n{summary}"
        elif file_extension == ".html":
            with open(file_path, 'r') as file:
                soup = BeautifulSoup(file, 'html.parser')
                content = soup.get_text()
                summary = content[:200]  # Mock summary for HTML
                return f"HTML Summary of {file_path}:\n{summary}"
        else:
            return f"Unsupported file type: {file_extension}. No summary available."
    except Exception as e:
        return f"An error occurred while processing the file: {e}"