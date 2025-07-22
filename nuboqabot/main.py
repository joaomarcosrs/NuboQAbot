import subprocess
import time
import requests
from decouple import config
from telegram.ext import ApplicationBuilder
from telegram.ext import MessageHandler, filters, CommandHandler
from .bot import start, quit, help, handle_pdf, handle_question
from .llm import MODEL


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
    time.sleep(2)

def pull_model(model=MODEL):
    subprocess.run(["ollama", "pull", model])

# Check and start Ollama if necessary
if not is_ollama_running():
    # Start Ollama
    start_ollama()
    pull_model(MODEL)

app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('quit', quit))
app.add_handler(CommandHandler('help', help))
app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question))

if __name__ == '__main__':
    app.run_polling()
