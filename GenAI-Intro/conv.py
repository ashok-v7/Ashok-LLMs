import openai
import os

from openai import OpenAI
messages = [{"role": "system", "content": "You are a helpful assistant."},]
client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get("OPENAI_KEY"),
)

# Keep repeating the following
while True:
    # Prompt user for input
    message = input("User: ")

    # Exit program if user inputs "quit"
    if message.lower() == "quit":
      break

    # Add each new message to the list
    messages.append({"role": "user", "content": message})

    # Request gpt-3.5-turbo for chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens= 50
    )

    # Print the response and add it to the messages list
    # Access the choices attribute of the response variable
    choices = response.choices

    # Get the first choice
    first_choice = choices[0]

    # Get the message content from the first choice
    chat_message = first_choice.message.content

    # Print the chat message
    print(f"Bot: {chat_message}")
    messages.append({"role": "assistant", "content": chat_message})