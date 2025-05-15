import streamlit as st
import os
import fitz
import datetime
from dotenv import load_dotenv
from app.ocr_extractor import extract_text_from_pdf
from app.summarizer import summarize_text
from app.classifier import classify_text
from app.router import send_to_zapier
from app.chatbot import build_chatbot_from_text
from app.mock_api import push_to_salesforce

load_dotenv()

st.title("AI Document Intelligence System")

uploaded_file = st.file_uploader("Upload a PDF document")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Metadata extraction
    doc = fitz.open("temp.pdf")
    page_count = len(doc)
    file_size = round(os.path.getsize("temp.pdf") / 1024, 2)
    upload_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    st.subheader("Document Metadata")
    st.write(f"Pages: {page_count}, Size: {file_size} KB, Uploaded: {upload_time}")

    text = extract_text_from_pdf("temp.pdf")
    st.subheader("Extracted Text")
    st.write(text[:1000])

    summary, key_points, action_items, sentiment = summarize_text(text)
    category = classify_text(text)

    st.subheader("Summary")
    st.write(summary)

    st.subheader("Key Points")
    st.write(key_points)

    st.subheader("Recommended Actions")
    st.write(action_items)

    st.subheader("Sentiment")
    st.write(sentiment)

    st.subheader("Category")
    st.write(category)

    zap_url = "https://hooks.zapier.com/hooks/catch/22929885/274mix8/"
    send_to_zapier({
    "summary": summary,
    "category": category,
    "sentiment": sentiment,
      "key_points": key_points,
    "recommended_actions": action_items
}, zap_url)
    st.success("Data sent to Zapier")
    if sentiment == "Negative" or category == "Legal":
        st.warning("Escalation Triggered: High-risk document")
        print("ALERT: Escalation triggered")

    # Salesforce Integration with Contact Email
    contact_email = st.text_input("Assign to Contact Email (optional)")
    if st.button("Push to Salesforce"):
        push_to_salesforce(summary, category, contact_email)

    # Document Intelligence Chatbot
    chatbot = build_chatbot_from_text([text])
    query = st.text_input("Ask something about the document")
    if query:
        answer = chatbot.run(query)
        st.subheader("AI Response")
        st.write(answer)
