# NuboQAbot

NuboQAbot is a Telegram bot based on RAG (Retrieval-Augmented Generation) that enables users to send PDF files and ask questions about the content of these documents.

The bot processes the PDF, extracts the text, generates semantic embeddings, and uses a local LLM (via Ollama) to provide contextual answers based on the uploaded content.

## Main features
- Upload PDF files directly through Telegram.
- Ask questions and receive answers grounded in the content of your documents.
- Local processing using pdfminer, Sentence Transformers, FAISS, and Ollama (e.g., Mistral model).

The goal is to enable intelligent, privacy-friendly document Q&A directly from your Telegram chat, without relying on external AI services.
