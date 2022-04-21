import os

import telebot
from config import TOKEN
import time

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('C:\\Users\\Vadym\\Documents\\GitHub\\vasadisimbot\\music\\'):
        if file.split('.')[-1] == "ogg":
            f = open('C:\\Users\\Vadym\\Documents\\GitHub\\vasadisimbot\\music\\' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id = msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.infinity_polling()
