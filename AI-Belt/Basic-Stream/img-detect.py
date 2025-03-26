import base64
from openai import OpenAI


# base64: The base64 module provides functions for encoding binary data to base64-encoded strings 
# and decoding base64-encoded strings back to binary data. 
# Base64 encoding is commonly used for encoding binary data in text-based formats such as JSON or XML.

# OpenAI: The OpenAI package is a Python client library for interacting with OpenAI's API. '
# 'The OpenAI class provides methods for accessing various OpenAI services, such as generating text, '
# 'performing natural language processing tasks, and more.



# Initialize an instance of the OpenAI class from the openai package,
client = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="xyz" # required by API but not used
)

# to send these images to GenAI model, we need them in a format it understands.
# This function takes the image_path as input and performs the following:

# Reads the image file from the specified path.
# Converts the image data into a base64-encoded string.
# Returns the resulting base64-encoded string.

# This encoded string is what we'll send to the AI model for a transforming an image file on your computer into a format that the AI model can understand and process.nalysis.

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "chef-ingredients.jpg" 
# Getting the base64 string 
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="llama3.2-vision:latest",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "What's in the Image?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)