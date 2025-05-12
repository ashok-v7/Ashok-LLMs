# Python LLM Works

This Python script processes restaurant review data, embeds it into a vector database, and enables efficient retrieval of similar reviews using vector search. Below is a detailed breakdown of its functionality:

## 1. Importing Libraries
The script imports the following modules:
- **OllamaEmbeddings**: For generating embeddings.
- **Chroma**: For managing the vector database.
- **Document**: For structuring the data.
- **os**: For file system operations.
- **pandas**: For handling tabular data.

## 2. Loading Data
The script reads a CSV file  into a Pandas DataFrame (`df`). This file is expected to contain restaurant reviews with the following columns:
- **Title**
- **Review**
- **Rating**
- **Date**

## 3. Embedding Model
An embedding model (`mxbai-embed-large`) is initialized using **OllamaEmbeddings**. This model converts textual data into numerical vectors for similarity searches.

## 4. Database Setup
The script checks if a directory (`./chrome_langchain_db`) exists to determine if the vector database has already been created. If the directory does not exist, the variable `add_documents` is set to `True`, indicating that documents need to be added to the database.

## 5. Document Preparation
If `add_documents` is `True`, the script processes the DataFrame rows to create **Document** objects. Each document contains:
- **page_content**: A combination of the review's title and content.
- **metadata**: Additional information such as the review's rating and date.
- **id**: A unique identifier for the document (based on the row index).

These documents are stored in a list (`documents`), and their IDs are stored in a separate list (`ids`).

## 6. Vector Store Initialization
A **Chroma** vector store is initialized with:
- **Collection Name**: `restaurant_reviews`
- **Persistence Directory**: `./chrome_langchain_db`
- **Embedding Function**: The embedding model

This vector store manages the storage and retrieval of the embedded documents.

## 7. Adding Documents
If `add_documents` is `True`, the prepared documents and their IDs are added to the vector store using the `add_documents` method. This step ensures the data is persisted for future use.

## 8. Retriever Setup
A retriever is created from the vector store using the `as_retriever` method. It is configured to return the top 5 most similar documents (`k=5`) for any given query.

---

### Summary
This script processes restaurant reviews, embeds them into a vector database, and sets up a retriever for similarity-based searches. It ensures the database is populated only once, making it efficient for repeated use.
