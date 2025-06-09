from flask import Flask, request
import telegram, os

TOKEN = os.environ['TELEGRAM_TOKEN']
bot = telegram.Bot(TOKEN)
app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text:
        chat_id = update.message.chat.id
        text = update.message.text
        bot.send_message(chat_id=chat_id, text=f"Received: {text}")
    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
