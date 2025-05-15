import os
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

load_dotenv()
llm = ChatOpenAI(model_name="gpt-4", temperature=0.3, openai_api_key=os.getenv("OPENAI_API_KEY"))

prompt = PromptTemplate(
    input_variables=["text"],
    template="""
Classify the following document into one of the categories: HR, Finance, Support, Legal, Engineering, Product, Marketing, Operations, Other.

Document:
{text}

Category:"""
)

classifier_chain = LLMChain(llm=llm, prompt=prompt)

def classify_text(text):
    return classifier_chain.run(text)
