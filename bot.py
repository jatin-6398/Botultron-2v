
import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters

# Environment variable se token lo
TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN environment variable not set")

bot = Bot(token=TOKEN)
app = Flask(__name__)

# Dispatcher setup (py-telegram-bot style)
dispatcher = Dispatcher(bot, None, use_context=True)

# Message handler
def echo(update, context):
    text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Received: {text}")

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Webhook endpoint
@app.route('/', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'OK'

# Health check (optional)
@app.route('/ping', methods=['GET'])
def ping():
    return 'pong', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
