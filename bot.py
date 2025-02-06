import telebot
from flask import Flask, request

# أدخل التوكن الخاص بالبوت هنا
API_TOKEN = 'import telebot
from flask import Flask, request

# أدخل التوكن الخاص بالبوت هنا
API_TOKEN ='7423708895:AAEeGH_lqZfNas69Yx98YSzTFdtj-xcLu58'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def home():
    return "بوت تليجرام يعمل 🎉"

# تعيين الـ Webhook
def set_webhook():
    webhook_url = 'https://your-bot-name.onrender.com/webhook'  # استبدلها برابط سيرفرك
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    set_webhook()  # إعداد Webhook عند تشغيل البوت
    app.run(host="0.0.0.0", port=10000)
'
bot = telebot.TeleBot(API_TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@app.route('/')
def home():
    return "بوت تليجرام يعمل 🎉"

# تعيين الـ Webhook
def set_webhook():
    webhook_url = 'https://your-bot-name.onrender.com/webhook'  # استبدلها برابط سيرفرك
    bot.remove_webhook()
    bot.set_webhook(url=webhook_url)

if __name__ == "__main__":
    set_webhook()  # إعداد Webhook عند تشغيل البوت
    app.run(host="0.0.0.0", port=10000)
