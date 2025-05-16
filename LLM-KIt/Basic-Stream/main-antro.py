import anthropic
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = anthropic.Anthropic(
    api_key = os.environ["ANTHROPIC_API_KEY"],
)

message = client.messages.create(
    model = "claude-3-5-sonnet-20241022",
    max_tokens = 8192,
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "what is the capital of the United States?",
                },
            ],
        },
    ],
)

print(message.content)