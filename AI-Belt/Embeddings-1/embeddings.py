import spacy
import pandas as pd

# load a spacy language model instead of open ai text embedding model-ada-002
nlp = spacy.load('en_core_web_sm')

with open('paragraph.txt', 'r',encoding="utf-8") as file:
    paragraph = file.read()



#process the paragraph using spacy
doc = nlp(paragraph)

#store vector representation
vectors = []

#Iteratre through the words in the paragraph and append their   vectors to the list
for token in doc:
    vectors.append(token.vector)


#create a dataframe to store the vectors
df = pd.DataFrame(vectors)

#save the vectors to a csv file
df.to_csv('embeddings.csv', index=False)


'''
paragraph = """
The AI Toolkit for VS Code (AI Toolkit) is a VS Code extension that enables you to download, test, fine-tune, and deploy AI models with your apps or in the cloud. For more information, see the AI Toolkit overview.
Install the AI Toolkit for VS Code
Download a model from the catalog
Run the model locally using the playground
Integrate an AI model into your application using REST or the ONNX Runtime

'''