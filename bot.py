from flask import Flask, request, Response
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, Dispatcher

import os

BOT_TOKEN = os.environ['BOTTOKEN']
app = Flask(__name__)
bot_app = ApplicationBuilder().token(BOT_TOKEN).build()
dispatcher: Dispatcher = bot_app.dispatcher

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Ultron here! Hello, {update.effective_user.first_name} 🤖")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot_app.bot)
    dispatcher.process_update(update)
    return Response('ok', status=200)

@app.route('/')
def health():
    return "🤖 Ultron is running!"

if __name__ == '__main__':
    app.run()
