
import openai
import os

from openai import OpenAI
messages = [{"role": "system", "content": "You are a helpful assistant."},]
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get("OPENAI_KEY"),
)

logs = """
Mar 25 12:30:01 sshd[12345]: Failed password for root from 192.168.1.10 port 34567
Mar 25 12:32:45 sshd[12346]: Accepted password for admin from 10.0.0.5 port 2222
"""
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a cybersecurity analyst. Identify suspicious activity in logs."},
        {"role": "user", "content": f"Analyze these logs:\n{logs}"}
    ]
)

print(response.choices[0].message.content)
