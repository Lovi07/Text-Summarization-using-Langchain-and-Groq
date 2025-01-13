LangChain: Summarize Text from YouTube, Websites, or PDF
This Streamlit app allows you to summarize content from various sources like YouTube videos, websites, or uploaded PDF files. The app uses LangChain, Groq, and LangSmith to process and summarize content.

Features:
Summarize content from YouTube videos by providing a URL.
Summarize text from any website by providing its URL.
Summarize content from PDF files by uploading the file directly.
Integration with LangSmith for tracking and API key management.
Powered by Groq API for the language model, utilizing gemma2-9b-it for summarization.
Requirements:
Python 3.10
Streamlit: For creating the app interface.
LangChain: For managing language models and prompts.
LangChain_Groq: To interact with Groq language models.
LangChain_Community: For loading documents from various sources.
validators: To validate URL inputs.
Temporary files: For managing PDF uploads.
PyPDFLoader: To extract content from PDF files.
Installation:
Clone the repository:

bash
Copy code
git clone <repository_url>
Install dependencies: If you don't have the dependencies installed, you can install them using pip. It is recommended to use a virtual environment:

Copy code
pip install -r requirements.txt
Set up API Keys:

Groq API Key: You will need a Groq API Key to use the language model. You can obtain it from the Groq platform.
LangSmith API Key: You will also need a LangSmith API Key for tracking. You can get it from the LangSmith platform.
Configuration:
Set your API keys in the sidebar:

Groq API Key: Enter your Groq API key.
LangSmith API Key: Enter your LangSmith API key.
Provide either a YouTube URL or Website URL for summarization, or upload a PDF file.

Usage:
Summarize a YouTube Video:

Paste the YouTube video URL in the provided text input and click the "Summarize the Content" button. The app will load the video content and generate a summary.
Summarize a Website:

Paste any website URL (e.g., blog post, article) into the input field and click the "Summarize the Content" button. The app will load the page content and generate a summary.
Summarize a PDF:

Upload a PDF file using the file uploader and click the "Summarize the Content" button. The app will process the file and provide a summary.
View Summary:

After processing, the app will display the generated summary.
Example:
YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Website URL: https://example.com/article
PDF Upload: Upload a file such as document.pdf
Troubleshooting:
Error: Missing API Keys:

Make sure you enter both the Groq API key and LangSmith API key in the sidebar.
Invalid URL:

Ensure that the URL entered is valid. The app only supports YouTube and website URLs.
Exception in Processing:

If an error occurs while processing the content, the app will display an exception message. Double-check your input and try again.
License:
This project is licensed under the MIT License - see the LICENSE file for details.
