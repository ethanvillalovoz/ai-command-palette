import os
from openai import OpenAI
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_file(file_path):
    """Process a file and provide AI-powered summarization, sentiment analysis, and keyword extraction."""
    try:
        if not os.path.isfile(file_path):
            return {"error": f"File not found: {file_path}"}

        _, file_extension = os.path.splitext(file_path)

        # Read the file content based on its type
        if file_extension == ".pdf":
            reader = PdfReader(file_path)
            content = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
        elif file_extension in [".txt", ".md", ".json", ".html"]:
            with open(file_path, 'r', encoding="utf-8") as file:
                content = file.read()
        else:
            return {"error": f"Unsupported file type: {file_extension}"}

        # Prepare the instructions and input for the OpenAI API
        instructions = """
        You are an AI assistant. Analyze the following text and provide:
        1. A concise summary.
        2. The overall sentiment (positive, negative, or neutral).
        3. Key phrases or topics extracted from the text.
        """
        input_text = content

        # Call the OpenAI API
        response = client.responses.create(
            model="gpt-4.1-nano",
            instructions=instructions,
            input=input_text,
        )

        return {"summary": response.output_text}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}