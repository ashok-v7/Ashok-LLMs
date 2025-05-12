
**Langchain Framework**

**Explore the available models  and Used AI Toolkit as a plugin** 

**Loading the model locally - using playground and ONNX**

**Created a  GenAI applications by using the models running on local VS Code AI Toolkit environment**

**Created a web-based chat interface using streamlit where users can input queries, which are then sent to an AI model via a local OpenAI API server. The AI's responses are displayed back in the chat interface, facilitating a conversational interaction**

**Developed a Food Chef App  using the cutting-edge Llama Vision Model** 




![alt text](<1.png>)


***✨ ASHOK-LLM's***

A brief description of your project and its purpose.

## 📑 Table of Contents

- [About the Project](#-about-the-project)
- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Prerequisites](#-prerequisites)
  - [Installation](#-installation)
- [Usage](#-usage)
- [Program List](#-program-list)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 📖 About the Project

Provide a high-level overview of Concepts to understand. Explain what it does and why it is useful.

## ✨ Features

- Feature 1 - Basic-Stream
- Feature 2 - Embeeding-Stream
- Feature 3 - Langchain Stream
- Feature 4 - GenAI-Intro

## 🚀 Getting Started

### 📋 Prerequisites

List the software and versions needed before using your project.

- Python 3.x and other python libraries

### 🛠️ Installation
 
1. Set up the virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   conda create -p venv python==3.10 -y
   conda activate /home/folder/venv
   pip install -r requirements.txt
   ```

## 📊 Usage
### Reasonin Models - 
    OpenAI o1 , o3-mini, o1-mini, DeepSeek-R1
    Usecases : Scientific reasoning , legal analysis, complex problem solving
    AI Agents with multi step descision making 
                    

### General Purpose LLMs : 
     -- Gpt 4o , Llama3.3 ,Claude
     Usecases : chatbots, Text summarization , content generation, Q&A , code completion  

***Intro to Embedding Models
   Embedding Model usecase
   Intro to RAG
   RAG Usecase
   RAG - Coding***

### Why is Chunking Needed for Large Documents in LangChain?
When working with large documents in LangChain, chunking is the process of splitting the document into smaller, manageable parts (or chunks). This is essential because Large Language Models (LLMs) have token limits—meaning they can only process a limited amount of text at once.

### Why Do We Need Chunking?
LLM Token Limits: LLMs like OpenAI’s GPT models can only handle a fixed number of tokens (e.g., GPT-4: ~128k tokens). Large documents may exceed this limit.

Efficient Retrieval: Chunking allows the system to search and retrieve the most relevant pieces of information.

Reduced Latency & Costs: Smaller chunks mean faster responses and lower costs when interacting with LLMs.

Better Context Understanding: Proper chunking with overlap maintains context between sections of a document.


### RAG is a technique that enhances large language models by retrieving relevant information from external knowledge sources before generating responses.
RAG consists of 3 phases
1. Retrieval Phase : 
The retrieval phase is responsible for finding the most relevant information from your knowledge sources. This consists of sub-tasks such as query processing, semantic search, vector similarity, filtering/ranking and various retrieval strategies (possibly across multiple datastores)
2. Augmentation Phase :
The augmentation phase bridges retrieval and generation by preparing and integrating the retrieved information. 
This consists of various sub-tasks such as context selection, context formatting, prompt engineering/rewriting, metadata integration and reranking
3. Generation Phase : 
The generation phase produces the final response based on the user query and augmented context. This can consists of subtasks such as prompt construction, LLM processing, citation generation, response refinement and confidence scoring.


### What problems does RAG solve
1. RAG Architecture is an improvement over standalone LLMs, because of
Knowledge cutoffs
2. LLMs have fixed knowledge as of their training date, while RAG can access up-to-date information
Hallucinations
3. LLMs may generate plausible but incorrect information, while RAG grounds responses in factual sources
4. Domain expertise
• LLMs have generalized knowledge, while RAG can access specialized
information
5. Private data access
   LLMs don't know your organization's private information, while RAG can connect to proprietary data



 
| **Component**             | **Module**                           | **Purpose**                                                                                       | **Usage**                                                                                           |
|---------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Streamlit**             | `streamlit`                         | Streamlit is a Python library used to create interactive web applications, especially for ML/AI.   | The `st` alias is used to access Streamlit's functions.                                              |
| **ChatOpenAI**            | `langchain_openai`                   | Provides an interface to interact with OpenAI's language models.                                   | Used to initialize and configure the OpenAI model for generating responses based on user input.      |
| **Chroma**                | `langchain_community.vectorstores`   | A vector store for storing and retrieving high-dimensional vectors for similarity searches.         | Typically used in applications requiring document retrieval or question-answering systems.            |
| **SentenceTransformerEmbeddings** | `langchain_community.embeddings`   | Generates embeddings using models from the Sentence Transformers library.                           | Converts text into embeddings to be stored in vector stores like Chroma for similarity searches.     |
| **StrOutputParser**       | `langchain_core.output_parsers`      | Parses the output from the language model into a string format.                                    | Converts the raw output from the language model into a usable string format for display or processing.|
| **ChatPromptTemplate**    | `langchain_core.prompts`             | Creates and manages prompt templates for interacting with the language model.                       | Used to create structured and consistent prompts for querying the language model.                    |
| **RunnableParallel**      | `langchain_core.runnables`           | Runs multiple tasks concurrently. Useful for parallel operations like retrieving multiple pieces.   | Manages and executes multiple tasks in parallel.                                                     |
| **RunnablePassthrough**   | `langchain_core.runnables`           | Passes the input through without modification. Useful as a placeholder.                             | Used to pass data through a pipeline without any changes.                                            |
 


## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

##  – V Ashok  – [LinkedIn](https://www.linkedin.com/in/ashokvanga/)
