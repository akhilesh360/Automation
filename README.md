# AI Document Intelligence

[![Live Demo](https://img.shields.io/static/v1?label=Streamlit&message=Demo&color=blue)](https://automation-ddwvwyexfe56f6s6bcowz5.streamlit.app/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  
[![Python ≥3.8](https://img.shields.io/badge/python-3.8%2B-blue.svg)]()

# AI Document Intelligence System

View live demo: https://automation-ddwvwyexfe56f6s6bcowz5.streamlit.app/

![Flowcharts](https://github.com/user-attachments/assets/2c8a73fc-0756-43c9-8067-57e7aa3d0c33)

This project is an AI-powered document intelligence system built with Streamlit. It processes PDF documents to extract text, summarize content, classify categories, analyze sentiment, and provide actionable insights. It also integrates with external services like Zapier and Salesforce for workflow automation.





## Features

- **PDF Text Extraction**: Extracts text from uploaded PDF documents. <img width="1077" alt="Screenshot 2025-05-15 at 7 55 08 AM" src="https://github.com/user-attachments/assets/ab0c3055-f50d-4f58-8af9-8226f3007bb9" />

  
- **Summarization**: Generates a concise summary, key points, and recommended actions.
- **Sentiment Analysis**: Analyzes the sentiment of the document (Positive, Neutral, or Negative).<img width="1077" alt="Screenshot 2025-05-15 at 7 55 19 AM" src="https://github.com/user-attachments/assets/647b0bb8-0893-4c86-ac76-cb08aa7b748f" />
- **Category Classification**: Classifies the document into predefined categories (e.g., HR, Finance, Legal, etc.).


- **Zapier Integration**: Sends extracted insights to a Zapier webhook.
<img width="717" alt="Screenshot 2025-05-15 at 7 56 39 AM" src="https://github.com/user-attachments/assets/901e3ccc-495e-4be5-b1f6-97c1ba360c99" />


- **Salesforce Integration**: Creates tasks in Salesforce with the extracted insights. <img width="1082" alt="Screenshot 2025-05-15 at 7 58 27 AM" src="https://github.com/user-attachments/assets/4c0b693a-a584-4faf-8f1a-15d29542e437"/>
- **AI Chatbot**: Allows users to query the document using an AI-powered chatbot. <img width="780" alt="Screenshot 2025-05-15 at 8 44 21 AM" src="https://github.com/user-attachments/assets/7fa709b7-22d0-4127-b864-beaa27dac2ba" />






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

