# AI Document Intelligence System

This project is an AI-powered document intelligence system built with Streamlit. It processes PDF documents to extract text, summarize content, classify categories, analyze sentiment, and provide actionable insights. It also integrates with external services like Zapier and Salesforce for workflow automation.

## Features

- **PDF Text Extraction**: Extracts text from uploaded PDF documents.
- **Summarization**: Generates a concise summary, key points, and recommended actions.
- **Sentiment Analysis**: Analyzes the sentiment of the document (Positive, Neutral, or Negative).
- **Category Classification**: Classifies the document into predefined categories (e.g., HR, Finance, Legal, etc.).
- **Zapier Integration**: Sends extracted insights to a Zapier webhook.
- **Salesforce Integration**: Creates tasks in Salesforce with the extracted insights.
- **AI Chatbot**: Allows users to query the document using an AI-powered chatbot.

## Project Structure

.env .gitignore main.py requirements.txt app/ chatbot.py classifier.py mock_api.py ocr_extractor.py router.py summarizer.py


- **`main.py`**: The entry point of the Streamlit application.
- **`app/`**: Contains modular components for text extraction, summarization, classification, chatbot, and integrations.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. Install dependencies:
pip install -r requirements.txt
3. Set up environment variables:
- Create a .env file in the root directory.
- Add the following variables:
  
- **OPENAI_API_KEY=** <XYZ>
- **SF_USERNAME=<XYZ>**
- **SF_PASSWORD=<XYZ>**
- **SF_TOKEN=<XYZ>**

Usage
1. Run the Streamlit application:
streamlit run [main.py](http://_vscodecontentref_/8)

2. Upload a PDF document in the web interface.

3. View extracted metadata, text, summaries, and insights.

4. Optionally:

Send data to Zapier.
Push tasks to Salesforce.
Query the document using the chatbot.

Dependencies
The project requires the following Python libraries (see requirements.txt for details):

- streamlit
- langchain
- openai
- fitz (PyMuPDF)
- faiss-cpu
- requests
- python-dotenv
- simple-salesforce

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
LangChain for LLM-based chains.
Streamlit for the web interface.
OpenAI for GPT-4 integration.
PyMuPDF for PDF text extraction.
FAISS for vector search.
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

