import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 


@bot.message_handler(commands=['start'])
def start(message):
        bot.reply_to(message,"Привет, это бот который будет кидать вам рандомных покемонов")
        bot.reply_to(message,"все команды тут ---> /info")

@bot.message_handler(commands=['info'])
def info(message):
        bot.reply_to(message,"/go - создать покемона")
        bot.reply_to(message,"/plus_age - вырастить покемона")


@bot.message_handler(commands=['go'])
def go(message):
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())

@bot.message_handler(commands=['plus_age'])
def age(message):
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.plus_age())





bot.infinity_polling(none_stop=True)
