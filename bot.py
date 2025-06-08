import telebot
from flask import Flask, request

TOKEN = "8070069668:AAHD6Yr5DpiK7vxYsAxKmLAd1xKKZ7irRK8"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "🤖 Botultron active hai! Tumne likha: " + message.text)

@app.route("/" + TOKEN, methods=["POST"])
def getMessage():
    json_str = request.stream.read().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://botultron.onrender.com/" + TOKEN)
    return "Webhook set!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
