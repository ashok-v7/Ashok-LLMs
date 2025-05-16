"""Run this model in Python

> pip install openai
"""
from openai import OpenAI

client = OpenAI(
    base_url = "http://localhost:11434/v1",
    api_key = "unused", # required for the API but not used
)

response = client.chat.completions.create(
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What is the capital of the United States?",
                },
            ],
        },
    ],
    model = "mistral-7b-v02-int4-cpu",
    max_tokens = 80000,
    temperature = 0.6,
)

print(response.choices[0].message.content)
# print(response.choices[0].message.content.split("\n\n")[-1])