import config
import telebot, random
from random import choice

API_TOKEN = config.token

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['random'])
def random_message(message):
    random_number = random.randint(1,100)
    bot.reply_to(message, random_number)


@bot.message_handler(commands=["joke"])
def message_joke(message):
    jokes = choice(["Доктор, у меня раздвоение личности. Ничего страшного, платите за двоих", "Знаете, почему программисты пьют кофе? Потому что без Java жизни нет!", "поел мужик дрожжей с сахаром. теперь ходит-бродит"])
    bot.reply_to(message, jokes)

bot.infinity_polling()