# LLM Engineering Practice

This repository contains practice of Large Language Models (LLMs), Prompt Engineering, LangChain, Retrieval-Augmented Generation (RAG), FastAPI, GitHub APIs, Webhooks, Background Tasks, and Backend Development using Python.

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

### Memory Concepts

### RAG Basics

* Document Loaders
* LangChain Documents
* page_content and metadata
* Text Chunking
* chunk_size
* chunk_overlap

### Embeddings

* Embedding Vectors
* Cosine Similarity
* Semantic Search

### ChromaDB

* Vector Stores
* Similarity Search
* Retrievers
* Retrieval Process

### Complete RAG Pipeline

* Context Injection
* Question Answering using RAG

### FastAPI & Backend Development

* FastAPI Basics
* CRUD APIs
* Pydantic Schemas
* Request & Response Handling
* SQLite
* PostgreSQL
* SQLAlchemy ORM
* Database Models
* Query Operations
* REST APIs

### GitHub REST API

* Personal Access Tokens
* Authentication Headers
* Repository API
* Pull Request API
* Contributor Analytics
* JSON Response Handling

### GitHub Webhooks

* Webhook Events
* Push Events
* Pull Request Events
* Event Payloads
* Event Headers
* ngrok Integration
* Real-Time Event Processing

### Background Tasks

* FastAPI BackgroundTasks
* add_task()
* Asynchronous Processing
* Webhook Event Processing
* Event Logging

### Event Storage & Analytics

* SQLite Event Database
* SQLAlchemy Models
* Database Sessions
* Event Storage
* Analytics APIs

---

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
│   ├── 07_retriever.py
│   ├── 08_rag_pipeline.py
│   └── notes.md
│
├── github-api/
│   ├── 01_repo_info_fetcher.py
│   ├── 02_pr_tracker.py
│   ├── 03_contributor_analytics.py
│   ├── 04_webhook_practice.py
│   ├── 05_background_tasks.py
│   ├── 06_webhook_background_task.py
│   ├── 07_event_logger.py
│   ├── 08_event_database.py
│   ├── 09_webhook_database.py
│   ├── 10_analytics_api.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── README.md
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
* Retrieval Systems
* FastAPI
* SQLAlchemy
* SQLite
* GitHub REST API
* GitHub Webhooks
* Background Tasks
* ngrok
* Environment Variables
* Git & GitHub