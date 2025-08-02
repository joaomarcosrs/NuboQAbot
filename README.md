# NuboQAbot

NuboQAbot is a Telegram bot based on RAG (Retrieval-Augmented Generation) that enables users to send PDF files and ask questions about the content of these documents.

The bot processes the PDF, extracts the text, generates semantic embeddings, and uses a local LLM (via Ollama) to provide contextual answers based on the uploaded content.

## Main features
- Upload PDF files directly through Telegram.
- Ask questions and receive answers grounded in the content of your documents.
- Local processing using pdfminer, Sentence Transformers, FAISS, and Ollama (e.g., Mistral model).

The goal is to enable intelligent, privacy-friendly document Q&A directly from your Telegram chat, without relying on external AI services.

## Prerequisites
- [Python3.12+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)
- [Docker](https://docs.docker.com/get-docker/)

## How to use

1. Clone the repository:

```bash
git clone https://github.com/joaomarcosrs/NuboQAbot.git
cd NuboQAbot
```

2. Create a `.env` file in the project root with the following content (example):

```env
TELEGRAM_TOKEN=your_telegram_token
OLLAMA_SERVER=http://localhost:11434
MODEL=mistral
SENTENCE_TRANSFORMER=all-MiniLM-L6-v2
```

3. Build the Docker image:

```bash
docker build -t nuboqabot .
```

4. Run the container:

```bash
docker run -d --env-file .env nuboqabot
```

The bot will be available and ready to receive PDFs and questions via Telegram.
