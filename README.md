# CS415 Assignment 01: FastAPI Modularization & Ollama Integration

A comprehensive guide and repository for Assignment 01. This project covers two main modules:
1. **Part 1**: Refactoring a single-file FastAPI application into a clean, modular architecture based on the **Single Responsibility Principle (SRP)**.
2. **Part 2**: Programmatic integration with Large Language Models (LLMs) using **Ollama API** via both **Local Execution** (`qwen2.5:1.5b`) and **Cloud Execution** (`llama3.2`).

---

## 📋 Table of Contents
- [1. Prerequisites & Environment Setup](#1-prerequisites--environment-setup)
- [2. Installing the Modern Tools (`uv` Manager)](#2-installing-the-modern-tools-uv-manager)
- [3. Project Structure](#3-project-structure)
- [4. Part 1: FastAPI Code Modularization](#4-part-1-fastapi-code-modularization)
- [5. Part 2: Ollama LLM Integration](#5-part-2-ollama-llm-integration)
- [6. Requirements File (`requirements.txt`)](#6-requirements-file-requirementstxt)
- [7. Protecting Secrets (`.gitignore`)](#7-protecting-secrets-gitignore)
---

## 1. Prerequisites & Environment Setup

Before starting, ensure you have Python (version 3.10 or higher) or Anaconda/Miniconda installed on your machine.

### Step 1: Create a Virtual Environment
It is recommended to run this project inside an isolated virtual environment.

Using standard Python:
```bash
python -m venv .venv
```

Or using Conda:
```bash
conda create -n cs415_env python=3.11 -y
conda activate cs415_env
```

---

## 2. Installing the Modern Tools (`uv` Manager)

`uv` is an extremely fast Python package manager written in Rust. It replaces `pip` and speeds up installation by up to 100x.

### Installing `uv`
Run the following command in your terminal:
```bash
pip install uv
```

Verify installation:
```bash
uv --version
```

---

## 3. Project Structure

Organize your project directory (`task1`) as follows:

```text
task1/
│
├── .env                  # Secret API Keys (DO NOT upload to GitHub)
├── .gitignore            # Git ignore configuration
├── requirements.txt      # Project dependencies
├── README.md             # Complete project documentation
│
├── models.py             # Part 1: Pydantic schemas & validations
├── logic.py              # Part 1: Core business logic
├── routes.py             # Part 1: FastAPI routers & endpoints
├── main.py               # Part 1: FastAPI app entrypoint
│
├── local_ollama.py       # Part 2: Method 1 (Local Model)
└── cloud_ollama.py       # Part 2: Method 2 (Cloud Model)
```

---

## 4. Part 1: FastAPI Code Modularization

The original monolithic script has been decomposed into four single-purpose modules to maintain clean code architecture.

### Module Roles
* **`models.py`**: Defines data structures (`Ticket` and `TicketResult`) using Pydantic. Handles input validation.
* **`logic.py`**: Contains pure python domain logic (`classify_ticket`). Parses support ticket messages and assigns categories.
* **`routes.py`**: Utilizes FastAPI's `APIRouter` to map HTTP requests.
* **`main.py`**: Initializes the FastAPI instance and registers the router.

### Running the FastAPI Application

Install required FastAPI components:
```bash
uv pip install "fastapi[standard]" pydantic
```

Run the development server:
```bash
uv run fastapi dev main.py
```
Access the interactive API documentation (Swagger UI) at:
👉 **`http://127.0.0.1:8000/docs`**

---

## 5. Part 2: Ollama LLM Integration

Programmatic chat interface with AI models using HTTP POST requests.

### Method 1: Local Ollama Model
1. Install Ollama from [ollama.com](https://ollama.com).
2. Pull the model using your terminal:
   ```bash
   ollama pull qwen2.5:1.5b
   ```
3. Run the Python script or Jupyter Notebook cell:
   ```python
   import requests

   question = "What is the capital of Egypt?"
   url = "http://localhost:11434/api/chat"
   payload = {
       "model": "qwen2.5:1.5b",
       "messages": [{"role": "user", "content": question}],
       "stream": False
   }

   response = requests.post(url, json=payload)
   print(response.json()["message"]["content"])
   ```

### Method 2: Cloud Ollama Model & API Keys
1. Sign up on Ollama Cloud and obtain your API Key.
2. Create a `.env` file in your root folder and paste your key:
   ```text
   OLLAMA_API_KEY=your_actual_api_key_here
   ```
3. Run the cloud interface script:
   ```python
   import os
   import requests
   from dotenv import load_dotenv

   load_dotenv()

   question = "What is the capital of Egypt?"
   url = "[https://ollama.com/api/chat](https://ollama.com/api/chat)"
   headers = {
       "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}",
       "Content-Type": "application/json"
   }
   payload = {
       "model": "llama3.2",
       "messages": [{"role": "user", "content": question}],
       "stream": False
   }

   response = requests.post(url, json=payload, headers=headers)
   print(response.json()["message"]["content"])
   ```

---

## 6. Requirements File (`requirements.txt`)

To reproduce the exact environment, place the following contents inside `requirements.txt`:

```text
# Part 1: FastAPI & Data Validation
fastapi[standard]
pydantic

# Part 2: Ollama API Integration (Local & Cloud)
requests
python-dotenv

# Interactive Environment
jupyter
notebook
```

Install all packages with one command:
```bash
uv pip install -r requirements.txt
```

---

## 7. Protecting Secrets (`.gitignore`)

Create a `.gitignore` file to avoid uploading sensitive files:

```gitignore
# Environment Variables & Secrets
.env
.env.*
*.env

# Python Cache & Artifacts
__pycache__/
*.py[cod]
*$py.class

# Virtual Environments
.venv/
venv/
ENV/
env/

# IDE & Tooling
.vscode/
.idea/
.ipynb_checkpoints/
.uv/
```

---

