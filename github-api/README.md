# GitHub API & Webhooks Practice

A collection of hands-on backend practice projects built with **Python, FastAPI, GitHub REST API, GitHub Webhooks, Background Tasks, SQLite, and SQLAlchemy**.


---

## Topics Covered

* GitHub REST API
* GitHub Authentication using Personal Access Tokens
* Repository Analytics
* Pull Request Tracking
* Contributor Analytics
* GitHub Webhooks
* ngrok for Local Webhook Testing
* FastAPI Background Tasks
* Event Logging
* SQLite Database
* SQLAlchemy ORM
* Analytics APIs

---

## Project Overview

### 01_repo_info_fetcher.py

Fetches repository information from GitHub.

**Features**

* Repository name
* Owner
* Language
* Stars
* Forks
* Open issues

---

### 02_pr_tracker.py

Tracks pull requests from a GitHub repository.

**Features**

* PR title
* Author
* State
* Created date
* Pull request URL

---

### 03_contributor_analytics.py

Analyzes repository contributors.

**Features**

* Top contributors
* Contribution counts
* Analytics summary

---

### 04_webhook_practice.py

Introduction to GitHub Webhooks using FastAPI.

**Features**

* Receive webhook payloads
* Parse GitHub events
* Handle JSON requests

---

### 05_background_tasks.py

Practice FastAPI Background Tasks.

**Features**

* Run tasks asynchronously after sending a response
* Simulate long-running jobs

---

### 06_webhook_background_task.py

Combines GitHub Webhooks with Background Tasks.

**Features**

* Receive GitHub events
* Process events in the background

---

### 07_event_logger.py

Stores webhook events in a log file.

**Features**

* Event logging
* Timestamp tracking
* Repository tracking

---

### 08_event_database.py

Introduction to SQLite and SQLAlchemy.

**Features**

* Database creation
* Event model creation
* Database connectivity

---

### 09_webhook_database.py

Stores GitHub webhook events directly in SQLite.

**Features**

* Webhook integration
* Database storage
* Background processing

---

### 10_analytics_api.py

Analytics API built using FastAPI and SQLite.

**Features**

* Retrieve stored GitHub events
* Event history API
* Analytics-ready data

---

## Technologies Used

* Python
* FastAPI
* Requests
* SQLAlchemy
* SQLite
* GitHub REST API
* GitHub Webhooks
* ngrok
* Background Tasks
* python-dotenv

---

## Installation

```bash
git clone <repository-url>
cd github-api

pip install -r requirements.txt
```

Create a `.env` file:

```env
GITHUB_TOKEN=your_github_personal_access_token
```

---

## Run FastAPI Applications

```bash
uvicorn filename:app --reload
```

Example:

```bash
uvicorn 10_analytics_api:app --reload
```

---

## Folder Structure

```text
github-api/
│
├── 01_repo_info_fetcher.py
├── 02_pr_tracker.py
├── 03_contributor_analytics.py
├── 04_webhook_practice.py
├── 05_background_tasks.py
├── 06_webhook_background_task.py
├── 07_event_logger.py
├── 08_event_database.py
├── 09_webhook_database.py
├── 10_analytics_api.py
├── database.py
├── models.py
├── requirements.txt
├── .env
├── .gitignore
├── events.db
└── README.md
```
