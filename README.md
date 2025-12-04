# 📘 Question-MCQs-Generator-Using-GenAI

## 🧠 Introduction

This project is an AI-powered tool that generates multiple-choice questions (MCQs) from uploaded PDFs or text inputs using **OpenAI GPT-4**, **LangChain**, and **Streamlit**. MCQs are essential for learning and assessment. By automating their generation using GenAI, this tool enables educators and learners to quickly generate relevant, context-based questions from any textual content, including research papers and study material.

---

## ✨ Features

1. Upload **PDF** or enter **custom text** for MCQ generation.  
2. Generate context-aware MCQs using **OpenAI GPT-4** with **LangChain**.  
3. Customize the number of questions you want to generate.  
4. Interactive and responsive UI built using **Streamlit**.  
5. Processes and handles multi-page PDFs using **PyPDF2**.  

---

## ⚙️ Technologies Used

- **Streamlit** – Web app interface for user interaction and display.  
- **OpenAI GPT-4** – Language model used for question and option generation.  
- **LangChain** – Framework for prompt handling, chaining, and RAG pipeline integration.  
- **PyPDF2** – Extracts raw text content from uploaded PDF files.  
- **dotenv** – Securely manages API keys and environment variables.

---

## 🚀 How It Works

### 📥 Input:
- Upload a **text-based PDF** file as input.
- Specify the number of MCQs to be generated.

### ⚙️ Processing:
- Text is extracted from the uploaded PDF using **PyPDF2**.
- Text is split into manageable chunks via **LangChain text splitters**.
- Questions and options are generated using **OpenAI GPT-4** via a custom prompt in a **LangChain LLMChain**.

### 📤 Output:
- The app displays the generated MCQs with 4 options (A–D), the correct answer, and explanation.
- All results are shown in real-time via the Streamlit web interface.

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.x  
- OpenAI API Key

### 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jayesh3103/text2test.git
   cd mcq-generator
2. **Set your OpenAI API key**:  
   Create a `.env` file in the project root and add the following line:
   ```ini
   OPENAI_API_KEY=your_openai_api_key_here
3. * Run the Streamlit app**:
     ```ini
     streamlit run app.py
---
### EXAMPLES

![image alt](https://github.com/SHUBHECHHAmondal/MCQ/blob/e1131db9a49d31741b3b1d0dbc138e75edf5fdb4/Screenshot%202025-07-08%20213016.png)
![image alt](https://github.com/SHUBHECHHAmondal/MCQ/blob/e6dafd8051213ce922e10d145ce4f2394666b79b/Screenshot%202025-07-08%20214123.png)


