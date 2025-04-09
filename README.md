# 🧠 RAG with Multi Data Source

This project demonstrates how to build a **Retrieval-Augmented Generation (RAG)** system using **multiple data sources** and **LangChain**. The RAG pipeline integrates data from Wikipedia, Arxiv, and LangSmith documentation using custom retriever tools. It utilizes the `llama2` model through Ollama for generating responses.

---

## 🔧 Features

- 📚 Query **Wikipedia** using `WikipediaQueryRun`
- 📄 Fetch papers from **Arxiv.org** with `ArxivQueryRun`
- 🌐 Ingest and search **LangSmith documentation** via web loader, FAISS, and retriever
- 🤖 Run LLM-based agents with `llama2` (Ollama integration)
- 🛠️ Use LangChain Tools and Agents framework for orchestration

---

## 🧰 Tech Stack

- [LangChain](https://python.langchain.com/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Ollama](https://ollama.com/)
- [Wikipedia API](https://pypi.org/project/wikipedia/)
- [Arxiv API](https://pypi.org/project/arxiv/)
- Python 3.12+
- `.env` support for environment configuration

---


## 🔁 RAG Architecture Flow

```mermaid
graph TD
    A[User Query] --> B[Agent Executor]
    B --> C1[Wikipedia Tool]
    B --> C2[Arxiv Tool]
    B --> C3[LangSmith Retriever Tool]

    C1 --> F[Wikipedia API]
    C2 --> G[Arxiv API]
    F --> H[Wikipedia Result]
    G --> I[Arxiv Result]

    C3 --> D[Web Page Documents via WebBaseLoader]
    D --> E[Split and Vectorize Documents with FAISS + OllamaEmbeddings]
    E --> C3

    H --> K[LLM Response]
    I --> K
    D --> K[LLM Response]

