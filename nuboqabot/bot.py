import os
from telegram import Update
from telegram.ext import ContextTypes
from loader import extract_text_from_pdf
from embedder import embed_text, create_or_update_index, model
from rag import retrieve_and_answer


PDF_FOLDER = 'pdfs'
os.makedirs(PDF_FOLDER, exist_ok=True)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Bot is on-line! Send a PDF.')

async def quit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.pop('chunks', None)
    context.user_data.pop('index', None)
    
    await update.message.reply_text("You've exited the current context. Upload a new PDF to get started.")

async def help(update: Update):
    await update.message.reply_text(
        'Available commands:\n'\
        '/start - Starts the bot\n'\
        '/help - Displays this help message\n'\
        '/clear - Clears all PDFs and session data\n'\
        '/quit - Exits the current PDF context\n'\
        '/list - Lists uploaded PDFs\n'\
        '/about - About the bot\n'\
    )

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    file_path = os.path.join(PDF_FOLDER, f'{file.file_unique_id}.pdf')
    
    await file.download_to_drive(
        custom_path=file_path
    )

    text = extract_text_from_pdf(
        file_path=file_path
    )
    
    chunks, embeddings = embed_text(text)

    context.user_data.setdefault('chunks', [])
    context.user_data['chunks'].extend(chunks)
    context.user_data['index'] =  create_or_update_index(
        index=context.user_data.get('index'),
        new_embeddings=embeddings
    )

    await update.message.reply_text('PDF Analyzed. Send a question about it!')

async def handle_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if 'index' not in context.user_data or 'chunks' not in context.user_data:
        await update.message.reply_text('Send a PDF first.')

    question = update.message.text
    answer = retrieve_and_answer(
        query=question,
        index=context.user_data['index'],
        chunks=context.user_data['chunks'],
        embedder_model=model
    )

    await update.message.reply_text(
        text=answer
    )


    