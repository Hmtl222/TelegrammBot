import telebot
from telebot import types

# Замени на свой токен от BotFather
TOKEN = "7987894291:AAFDHS7xSoetDTHbW-N36EVGWajKpKtrlak"
bot = telebot.TeleBot(TOKEN)


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    btn2 = types.KeyboardButton("❓ Помощь")
    btn3 = types.KeyboardButton("Расскажи о себе")
    btn4 = types.KeyboardButton("Помоги с задачей")
    markup.add(btn1, btn2)
    markup.add(btn3)
    markup.add(btn4)
    bot.send_message(message.chat.id,
                     "Добро пожаловать! Выбери кнопку 👇",
                     reply_markup=markup)


# Обработка сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "👋 Привет":
        bot.send_message(message.chat.id, "Привет-привет! ✋")
    elif message.text == "❓ Помощь":
        bot.send_message(message.chat.id, "Напиши, чем помочь! Я готов 🤖")
    elif message.text == "Расскажи о себе":
        bot.send_message(
            message.chat.id,
            "Я твой ИИ-помощник. Создан, чтобы помогать тебе, брат! 💪")
    else:
        bot.send_message(message.chat.id, "Я тебя не понял 🤖")
    if message.text == "Помоги с задачей":
        bot.send_message(message.chat.id, "Чем помочь?,Напиши")


# На всякий случай отключаем старый вебхук
bot.remove_webhook()

# Запускаем polling
bot.polling()
