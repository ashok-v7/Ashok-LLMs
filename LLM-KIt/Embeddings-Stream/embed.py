import spacy
import pandas as pd

# Load a spaCy language model
#instead of OpenAI Text-embedding-ada-002
nlp = spacy.load("en_core_web_md")  #python -m spacy download en_core_web_md. 

with open("paragraph.txt", "r", encoding="utf-8") as file:
    paragraph = file.read()

# Process the paragraph using spaCy
doc = nlp(paragraph)

# store vector representations
vectors = []

# Iterate through the words in the paragraph and append their vectors to the list
for token in doc:
    vectors.append(token.vector)

# Create a DataFrame to store the vectors
df = pd.DataFrame(vectors)

# Save the vectors to a CSV file
df.to_csv('embeddings.csv', index=False)

'''

# paragraph = """
Gemini 2.5 Pro Experimental is our most advanced model for complex tasks. It tops the LMArena leaderboard — which measures human preferences — by a significant margin, indicating a highly capable model equipped with high-quality style. 2.5 Pro also shows strong reasoning and code capabilities, leading on common coding, math and science benchmarks.

Gemini 2.5 Pro is available now in Google AI Studio and in the Gemini app for Gemini Advanced users, and will be coming to Vertex AI soon. We’ll also introduce pricing in the coming weeks, enabling people to use 2.5 Pro with higher rate limits for scaled production use.

Enhanced reasoning
Gemini 2.5 Pro is state-of-the-art across a range of benchmarks requiring advanced reasoning. Without test-time techniques that increase cost, like majority voting, 2.5 Pro leads in math and science benchmarks like GPQA and AIME 2025.

It also scores a state-of-the-art 18.8% across models without tool use on Humanity’s Last Exam, a dataset designed by hundreds of subject matter experts to capture the human frontier of knowledge and reasoning.

Advanced coding
We’ve been focused on coding performance, and with Gemini 2.5 we’ve achieved a big leap over 2.0 — with more improvements to come. 2.5 Pro excels at creating visually compelling web apps and agentic code applications, along with code transformation and editing. On SWE-Bench Verified, the industry standard for agentic code evals, Gemini 2.5 Pro scores 63.8% with a custom agent setup.

Here’s an example of how 2.5 Pro can use its reasoning capabilities to create a video game by producing the executable code from a single line prompt.


Building on the best of Gemini
Gemini 2.5 builds on what makes Gemini models great — native multimodality and a long context window. 2.5 Pro ships today with a 1 million token context window (2 million coming soon), with strong performance that improves over previous generations. It can comprehend vast datasets and handle complex problems from different information sources, including text, audio, images, video and even entire code repositories.

Developers and enterprises can start experimenting with Gemini 2.5 Pro in Google AI Studio now, and Gemini Advanced users can select it in the model dropdown on desktop and mobile. It will be available on Vertex AI in the coming weeks.

'''