import streamlit as st
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

# Load your OpenAI API Key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI LLM
llm = ChatOpenAI(openai_api_key=openai_api_key, temperature=0.5, model_name="gpt-4")

# Prompt Template for MCQ generation
mcq_template = PromptTemplate(
    input_variables=["context", "num_questions"],
    template="""
You are a helpful assistant that generates multiple-choice questions (MCQs) from context.

Context:
{context}

Generate {num_questions} MCQs from the above context. Each MCQ should include:
- A question
- 4 options labeled A, B, C, D
- The correct answer with explanation

Format:
Q1: ...
A. ...
B. ...
C. ...
D. ...
Answer: ...
Explanation: ...
"""
)

# LLM Chain
mcq_chain = LLMChain(llm=llm, prompt=mcq_template)

# PDF Text Extraction
def extract_text_from_pdf(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Streamlit UI
st.set_page_config(page_title="📘 MCQ Generator", layout="wide")
st.title("📘 Gen AI MCQ Generator")
st.markdown("Upload a text-based PDF and generate MCQs using OpenAI + LangChain.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
num_questions = st.number_input("Number of MCQs to generate", min_value=1, max_value=20, value=5)

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.success("PDF text extracted successfully!")

    if st.button("Generate MCQs"):
        with st.spinner("Generating MCQs..."):
            response = mcq_chain.run({"context": text[:3000], "num_questions": num_questions})
            st.markdown("### 📄 Generated MCQs:")
            st.text_area("Output", response, height=500)
