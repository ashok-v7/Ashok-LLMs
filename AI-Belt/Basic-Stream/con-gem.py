"""Run this model in Python

> pip install google-generativeai
"""
import os
import google.generativeai as genai

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "max_output_tokens": 20,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("Thanks")

print(response.text)