# LLM Engineering Practice

This repository contains practice of Large Language Models (LLMs), Prompt Engineering, LangChain, and Retrieval-Augmented Generation (RAG) using Python.

## Topics Covered

### LLM Concepts

* What are Large Language Models (LLMs)
* Tokens and Tokenization
* How LLMs generate responses

### API Integration

* API Calls
* Environment Variables (.env)
* Model Selection
* Response Handling

### Prompt Engineering

* System Prompts
* Assistant Roles
* Temperature Control
* Few-Shot Prompting
* Structured JSON Output

### Token Management

* Token Usage Monitoring
* Prompt Tokens
* Completion Tokens
* Cost Awareness

### LangChain Fundamentals

* ChatGroq
* PromptTemplate
* ChatPromptTemplate
* StrOutputParser
* Chains
* LCEL (LangChain Expression Language)
* invoke()
* batch()
* stream()
* Memory Concepts

### RAG Basics

* Document Loaders
* LangChain Documents
* page_content and metadata
* Text Chunking
* chunk_size
* chunk_overlap
* Embeddings
* Embedding Vectors
* Cosine Similarity
* Semantic Search
* ChromaDB
* Vector Stores
* Similarity Search

## Project Structure

```text
AI-ENGINEERING/
│
├── groq-api/
│   ├── 01_api_call.py
│   ├── 02_system_prompt.py
│   ├── 03_assistant_role.py
│   ├── 04_temperature.py
│   ├── 05_json_output.py
│   ├── 06_few_shot_prompting.py
│   ├── 07_token_usage.py
│   ├── notes.md
│   └── requirements.txt
│
├── langchain-basics/
│   ├── 01_langchain.py
│   ├── 02_prompt_template.py
│   ├── 03_output_parser.py
│   ├── 04_chain.py
│   ├── 05_chat_prompt_template.py
│   ├── 06_batch.py
│   ├── 07_stream.py
│   └── notes.md
│
├── rag-basics/
│   ├── 01_document_loader.py
│   ├── 02_text_splitter.py
│   ├── 03_embeddings.py
│   ├── 04_similarity.py
│   ├── 05_chromadb.py
│   ├── 06_chromadb_search.py
│   └── notes.md
│
└── README.md
```

## Technologies Used

* Python
* Groq API
* Llama Models
* LangChain
* ChromaDB
* Sentence Transformers
* Prompt Engineering
* RAG Concepts
* Semantic Search
* Vector Embeddings
* Environment Variables
* Git & GitHub
