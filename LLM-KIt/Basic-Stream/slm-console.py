"""Run this model in Python

> pip install openai
"""
from openai import OpenAI


query = input("Enter a query")

client = OpenAI(
    base_url = "http://localhost:5272/v1",
    api_key = "unused", # required for the API but not used
)

response = client.chat.completions.create(
        messages = [
        {
            "role": "user","content" : "You are an helpful assistant and provides structured answers",
             "role":"user","content" : query   },
            ],
        
    model = "Phi-3-mini-128k-cpu-int4-rtn-block-32-acc-level-4-onnx",
    max_tokens = 100,
    temperature = 0.7,
)

print(response.choices[0].message.content)
# print(response.choices[0].message.content.split("\n\n")[-1])