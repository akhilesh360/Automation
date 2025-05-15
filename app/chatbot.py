import os
from dotenv import load_dotenv
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4", temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

# Setup FAISS index (run once, persist for querying)
def build_chatbot_from_text(docs):
    db = FAISS.from_texts(docs, embedding)
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa