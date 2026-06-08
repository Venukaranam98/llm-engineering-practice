AI Engineering Notes -
1. What is an LLM?

LLM stands for Large Language Model.

It is an AI model trained on massive amounts of text data such as:

Books
Articles
Websites
Documentation
Research Papers

The model learns language patterns and can generate human-like responses.

Examples:

GPT
Llama
Qwen
Gemini
2. What are Tokens?

AI does not read text directly.

It first breaks text into smaller pieces called tokens.

Example:

I love FastAPI

becomes

["I", "love", "FastAPI"]

Sometimes words are split further:

"loving"

becomes

["lov", "ing"]

Tokens are the actual units processed by the model.

3. What are Embeddings?

Embeddings are numerical representations of words or sentences.

Example:

Dog
Cat
Car

might become:

[0.23, 0.81, ...]
[0.21, 0.79, ...]
[0.95, 0.10, ...]

Dog and Cat will have similar vectors.

Embeddings help AI understand meaning and similarity.

Used heavily in:

RAG
Semantic Search
Vector Databases
4. Training vs Inference
Training

The model learns from huge datasets.

Example:

Books
Articles
Websites

Training is expensive and done once.

Inference

Inference is when users ask questions.

Example:

User: What is FastAPI?

The trained model generates an answer.

5. Attention Mechanism

Attention helps the model focus on important words.

Example:

My laptop is out of charge.
It needs charging.

The model understands:

"It" = Laptop

by looking back at previous words.

6. System Prompt

A system prompt controls the model's behavior.

Example:

You are a senior Python mentor.

Now the model answers like a Python mentor.

7. Assistant Role

The assistant role contains previous AI responses.

It helps maintain conversation flow and context.

8. Temperature

Controls randomness.

temperature = 0
Same answer every time
Reliable
Deterministic
Best for production

Example:

DBMS = Database Management System

Always same answer.

temperature = 1
Some creativity
Slight variation
temperature = 1.8
Highly creative
More randomness
Different outputs

Used for:

Stories
Brainstorming
Startup Names
9. Few-Shot Prompting

Few-shot prompting means giving examples before asking the real question.

Example:

FastAPI -> Web Framework
Python -> Programming Language
PostgreSQL -> ?

Output:

Database

The model learns the pattern from examples.

10. JSON Output

We can force the model to respond in JSON format.

Example:

{
  "name": "Venu",
  "skills": ["Python", "FastAPI", "React"]
}

Useful for:

APIs
Automation
AI Agents
11. Token Usage

Every request consumes:

Prompt Tokens
Completion Tokens

Example:

Prompt Tokens = 61
Completion Tokens = 4
Total Tokens = 65

Total Tokens:

Prompt + Completion

Used for:

Cost Calculation
Monitoring Usage
12. API Call Flow
User Prompt
     ↓
Groq API
     ↓
LLM
     ↓
Generated Response
     ↓
Python Prints Output

Python code:

response = client.chat.completions.create(...)

This sends the request to the model and returns the response.