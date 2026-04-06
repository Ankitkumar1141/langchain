# 🦜🔗 LangChain Practicals

A hands-on collection of practical examples, notebooks, and projects built with [LangChain](https://www.langchain.com/) — covering everything from basic chains to advanced agentic workflows.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Repository Structure](#repository-structure)
- [Practicals Covered](#practicals-covered)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

This repository is a structured learning resource for mastering LangChain. Each folder contains self-contained, well-documented examples that progressively build from foundational concepts to production-ready patterns.

Whether you're just getting started with LLMs or building complex multi-agent systems, you'll find practical code you can run, modify, and learn from.

---

## Prerequisites

- Python 3.9+
- Basic understanding of Python
- API key(s) for at least one LLM provider (OpenAI, Anthropic, etc.)

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/langchain-practicals.git
cd langchain-practicals

# Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---
## Practicals Covered

| # | Topic | Description |
|---|-------|-------------|
| 01 | **Basics** | LLMs, Chat Models, and first chains |
| 02 | **Chains** | LLMChain, SequentialChain, RouterChain |
| 03 | **Prompts** | Prompt templates, few-shot, output parsers |
| 04 | **Memory** | Buffer, Summary, Entity, and Vector memory |
| 05 | **RAG** | Document loaders, splitters, embeddings, vector stores |
| 06 | **Agents** | ReAct, OpenAI Functions, and custom agents |
| 07 | **Tools** | Built-in and custom tools for agents |
| 08 | **Callbacks** | Logging, streaming, and custom callbacks |
| 09 | **LangSmith** | Tracing, debugging, and evaluation |
| 10 | **Projects** | End-to-end real-world applications |

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your credentials:

```bash
cp .env.example .env
```

```env
# LLM Providers
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
GOOGLE_API_KEY=your_google_key_here

# Vector Stores
PINECONE_API_KEY=your_pinecone_key_here
PINECONE_ENV=your_pinecone_environment

# LangSmith (optional but recommended)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key_here
LANGCHAIN_PROJECT=langchain-practicals
```

---

## Usage

Each practical is standalone. Navigate into any folder and run the script:

```bash
# Example: Run the RAG pipeline practical
cd 05_retrieval_rag
python rag_pipeline.py
```

For Jupyter notebooks:

```bash
jupyter notebook
```

---

## Contributing

Contributions are welcome! If you'd like to add a new practical or improve an existing one:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/add-new-practical`)
3. Commit your changes (`git commit -m 'Add: new practical on X'`)
4. Push to your branch (`git push origin feature/add-new-practical`)
5. Open a Pull Request

Please keep examples clean, well-commented, and beginner-friendly.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">
  Made with ❤️ for the LangChain community · Happy Learning! 🚀
</div>