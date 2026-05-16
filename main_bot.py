import telebot
import os
carimglist = os.listdir('carimages')
cityimglist = os.listdir('cityimages')
radioimglist = os.listdir('radioimages')
token = "8674064004:AAGIJQTYdPYEi8splqvG4_hhKVMYk_0RH4M"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Im the bot specialized in GTA universe info like vehicles, cities, characters, etc")

@bot.message_handler(commands=['help'])
def send_commands(message):
    bot.reply_to(message, "Here are the available commands: /start, /help, /car_examples, /city_examples")

@bot.message_handler(commands=['car_examples'])
def send_car(message):
    bot.reply_to(message, "Here are some examples of cars in the GTA universe:")
    for put in carimglist:
        with open(f'carimages/{put}', 'rb') as f:
            bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['city_examples'])
def send_city(message):
    bot.reply_to(message, "Here are some examples of cities in the GTA universe:")
    for put in cityimglist:
        with open(f'cityimages/{put}', 'rb') as f:
            bot.send_photo(message.chat.id, f) 

@bot.message_handler(commands=['radio_examples'])
def send_radio(message):
    bot.reply_to(message, "Here are some examples of radio stations in the GTA universe:")
    for put in radioimglist:
        with open(f'radioimages/{put}', 'rb') as f:
            bot.send_photo(message.chat.id, f) 

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
