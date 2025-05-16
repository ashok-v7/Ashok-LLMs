
# Import the OpenAI class from the openai module
from openai import OpenAI

# Get the user input
query=input("Enter query:")

# Create an instance of the OpenAI class
client = OpenAI(
    base_url="http://127.0.0.1:5272/v1/",
    api_key="xyz" # not used
)

# Call the chat completions endpoint include the prompt and model
chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user","content": "You are a helpful assistant and provides structured answers , "
        "If you do not know the answer then respond I dont know"},
        {"role": "user", "content": query}
    ],
    model="Phi-3-mini-128k-cpu-int4-rtn-block-32-acc-level-4-onnx",
)

# Print the response 
print(chat_completion.choices[0].message.content)