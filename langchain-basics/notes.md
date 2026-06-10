# LangChain Basics Notes

## What is LangChain?

LangChain is a framework used to build applications powered by Large Language Models (LLMs).

It helps connect:

- Prompts
- LLMs
- Output Parsers
- Memory
- Documents
- Retrieval Systems

---

## ChatGroq

ChatGroq is used to connect LangChain with Groq-hosted LLMs.

Example:

```python
llm = ChatGroq(
    model="llama3-8b-8192"
)
```

Purpose:

- Send prompts to Groq models
- Receive AI responses

---

## PromptTemplate

PromptTemplate creates reusable prompts.

Without PromptTemplate:

```python
"Explain FastAPI"
"Explain Python"
"Explain JWT"
```

With PromptTemplate:

```python
"Explain {topic}"
```

Example:

```python
prompt = PromptTemplate.from_template(
    "Explain {topic}"
)
```

Purpose:

- Reuse prompts
- Dynamic prompt generation

---

## ChatPromptTemplate

ChatPromptTemplate creates structured chat messages.

It separates:

- System Messages
- Human Messages
- AI Messages

Example:

```python
ChatPromptTemplate.from_messages([
    ("system", "You are a senior Python mentor"),
    ("human", "{question}")
])
```

Purpose:

- Define AI behavior
- Create conversational prompts

---

## StrOutputParser

StrOutputParser converts model output into a string.

Example:

```python
parser = StrOutputParser()
```

Purpose:

- Extract clean text responses
- Simplify output handling

---

## Chain

A Chain connects multiple AI steps together.

Example:

```python
chain = prompt | llm | parser
```

Flow:

Prompt
↓
LLM
↓
Parser
↓
Response

Purpose:

- Automate AI workflows
- Connect multiple components

---

## LCEL

LCEL stands for:

LangChain Expression Language

Example:

```python
chain = prompt | llm | parser
```

Purpose:

- Build chains using simple syntax
- Create readable AI pipelines

---

## invoke()

Used for:

Single Input → Single Output

Example:

```python
chain.invoke(
    {"topic": "FastAPI"}
)
```

Purpose:

- Generate one response at a time

---

## batch()

Used for:

Multiple Inputs → Multiple Outputs

Example:

```python
chain.batch([
    {"topic": "FastAPI"},
    {"topic": "JWT"},
    {"topic": "PostgreSQL"}
])
```

Purpose:

- Process multiple requests together

---

## stream()

Used for:

Streaming responses chunk-by-chunk.

Example:

```python
for chunk in chain.stream(
    {"topic": "FastAPI"}
):
    print(chunk)
```

Purpose:

- Real-time response generation
- Better user experience

---

## Memory

Memory stores previous conversation information.

Example:

User:

My name is Venu

Later:

What is my name?

Memory helps the AI answer correctly.

Purpose:

- Maintain conversation context
- Enable follow-up questions

---

## Summary

PromptTemplate
↓
ChatPromptTemplate
↓
LLM
↓
StrOutputParser
↓
Chain
↓
Response

Key Points:

- PromptTemplate creates reusable prompts.
- ChatPromptTemplate creates structured chat messages.
- StrOutputParser converts outputs into strings.
- Chains connect multiple AI steps together.
- invoke() handles single requests.
- batch() handles multiple requests.
- stream() returns responses in chunks.
- Memory stores conversation context.
- LCEL provides clean chain syntax.