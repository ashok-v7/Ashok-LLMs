import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
from dotenv import load_dotenv, dotenv_values
import os

# Load fresh values always
load_dotenv(dotenv_path=".env", override=True)

# Access updated value
#print("REFRESHED VALUE:", os.getenv("GEMINI_API_KEY"))

# Extract text from uploaded PDF files
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



# Split the text into manageable chunks
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

# Create and save a FAISS vector store from text chunks
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Create a QA chain using LangChain 3.0 pattern
def get_conversational_chain(vector_store):
    prompt_template = PromptTemplate(
        template="""
        Context:
{context}

        Question:
{question}

        Answer:
""",
        input_variables=["context", "question"]
    )

    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    document_chain = create_stuff_documents_chain(llm=model, prompt=prompt_template)
    qa_chain = document_chain.invoke({"input_documents": vector_store.as_retriever().get_relevant_documents(user_question), "question": user_question})
    return qa_chain

# Handle user input to get response
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    chain = get_conversational_chain(vector_store)
    response = chain.invoke({"question": user_question})
    st.write("Reply:", response["answer"])

# Streamlit UI
def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini 💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")

if __name__ == "__main__":
    main()