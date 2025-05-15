import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# 🔒 Secure key access using Streamlit Secrets
if "OPENAI_API_KEY" not in st.secrets:
    st.error("Missing OPENAI_API_KEY in Streamlit secrets")
    raise ValueError("OPENAI_API_KEY not found")

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.3,
    openai_api_key=st.secrets["OPENAI_API_KEY"]
)

def summarize_text(text):
    prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        Given the following business document, generate:
        1. A concise summary
        2. A bullet-point list of 3-5 key insights
        3. A list of recommended follow-up actions
        4. A sentiment analysis of the document (Positive, Neutral, or Negative)

        Document:
        {text}

        Return the results clearly labeled as:
        Summary:
        Key Points:
        Action Items:
        Sentiment:
        """
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    output = chain.run(text)

    summary = extract_between(output, "Summary:", "Key Points:")
    key_points = extract_between(output, "Key Points:", "Action Items:")
    action_items = extract_between(output, "Action Items:", "Sentiment:")
    sentiment = output.split("Sentiment:")[-1].strip()

    return summary.strip(), key_points.strip(), action_items.strip(), sentiment.strip()

def extract_between(text, start, end):
    try:
        return text.split(start)[1].split(end)[0].strip()
    except:
        return "[Parsing Error]"
