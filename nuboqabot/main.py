import subprocess
import time
import requests
from decouple import config
from telegram.ext import ApplicationBuilder
from telegram.ext import MessageHandler, filters, CommandHandler
from bot import start, handle_pdf, handle_question
from llm import MODEL


TOKEN = config('TELEGRAM_TOKEN', cast=str)
app = ApplicationBuilder().token(TOKEN).build()

def is_ollama_running():
    try:
        requests.get(config('OLLAMA_SERVER', cast=str))
        return True
    except Exception:
        return False

def start_ollama():
    subprocess.Popen(["ollama", "serve"])
    time.sleep(2)  # Espera o Ollama subir

def pull_model(model=MODEL):
    subprocess.run(["ollama", "pull", model])

# Checa e inicia Ollama se necessário
if not is_ollama_running():
    print("Init Ollama...")
    start_ollama()
    pull_model(MODEL)
else:
    print("Ollama is running.")

app.add_handler(CommandHandler('start', start))
app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

if __name__ == '__main__':
    app.run_polling()
