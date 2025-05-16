import streamlit as st
import os
from google.generativeai import GenerativeModel, configure
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API
configure(api_key=os.environ["GEMINI_API_KEY"])

# Initialize the Gemini model
client = GenerativeModel("gemini-1.5-pro",
            generation_config={
            "max_output_tokens": 30,
            "temperature": 0.7,
        })  # Adjust model name as needed

# client = OpenAI(
#     base_url="http://localhost:11434/v1/",
#     api_key="xyz" 
# )

st.title("Chat with Gemini 1.5 Pro")
query = st.chat_input("Enter query:")

if query:
    with st.chat_message("user"):
        st.write(query)

    # Generate response using Gemini API
    chat_completion = client.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": "You are a helpful assistant and provides structured answers."}
                ]
            },
            {
                "role": "user",
                "parts": [
                    {"text": query}
                ]
            }
        ]
    )

    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {"role": "user","content": "You are a helpful assistant and provides structured answers."},
    #         {"role": "user", "content": query}
    #     ],
    #     model="mistral-7b-v02-int4-cpu",
        
    # )

    with st.chat_message("assistant"):
        st.write(chat_completion.text)  # Adjust based on actual response structure
