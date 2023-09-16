import telebot
bot = telebot.TeleBot("6481921131:AAGxFf7HIMwmLYlgUQaG9MdWiFM2zxB4voo")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, message.from_user.username + ', добро пожаловать!, нажми на /help')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    global user_id
    user_id = message.from_user.id
    bot.send_message(user_id, 'Я бот, который ничего не умеет))), нажми на /start')

bot.infinity_polling()