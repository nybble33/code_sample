#!/usr/bin/python
import telebot;
from n_log import N_log

print('Start telebot')
bot = telebot.TeleBot('1842197193:AAHH55ZLId2UkgcA8u9BBfnOC7q_m8y8qGs')
_n_log = N_log('n_bot')

@bot.message_handler(commands=['start'])
def start_message(message):
    _n_log.write(str(message.from_user.id)+
                ' -- '+str(message.from_user.username)+
                ' -- '+str(message.chat.id)
                )
    bot.send_message(message.chat.id,
                    'Hey there from '+
                    str(message.chat.id)
                    )

@bot.message_handler(commands=['swear'])
def start_message(message):
    bot.send_message(message.chat.id,
                    'Fuck you, asshole!!!')


@bot.message_handler(content_types=['text'])
def start_message1(message):
    if message.text == 'who are you':
        bot.send_message(message.chat.id, 'I am a nybble bot!')

bot.polling()
