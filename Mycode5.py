# -*- coding: utf-8 -*-
#chat id457879646 dp - 279790872
import telebot
import logging
import emoji
import sys
import time
from telebot import types


TOKEN = '457879646:AAFKh5GQ0jvyzjr2_kJOAM_nSaq8_a0FIVQ'
bot = telebot.TeleBot(TOKEN)
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start', 'help'])
def start(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in
                   [emoji.emojize(':speech_balloon:About', use_aliases=True),
                    emoji.emojize(':city_sunrise:Map', use_aliases=True),
                    emoji.emojize(':question:Kahoot', use_aliases=True),
                    emoji.emojize(':clock10:Agenda', use_aliases=True),
                    emoji.emojize(':raising_hand:Question', use_aliases=True),
                    emoji.emojize(':white_check_mark:Vote', use_aliases=True),
                    emoji.emojize(':mailbox:Contacts', use_aliases=True)]])
    msg = bot.send_message(m.chat.id, 'Привет! Я виртуальный помощник, сопровождающий бизнес-завтрак Agile в PwC!\n'
                                      'Я могу выполнять различные команды с помощью кнопок внизу экрана.\n'
                                      'Hello! I am a virtual assistant supervising Agile Business Breakfast in PwC!\n'
                                      'I can perform different commands through the buttons in the bottom of your screen',
                           reply_markup=keyboard)
    bot.send_chat_action(m.chat.id, 'typing')
    time.sleep(3)
    msg = bot.send_message(m.chat.id, 'Чем я могу вам помочь?\n'
                                      'How can I help you?', reply_markup=keyboard)

@bot.message_handler(func=lambda message: 'About' in message.text)
def about(m):
    bot.send_message(m.chat.id, 'К сожалению, в настоящий момент я не могу поддерживать с вами полноценный диалог, '
                                'однако вы можете сделать мне один из запросов ниже:\n'
                                'Запросить описание моего функционала - About\n'
                                'Запросить карту со схемой проезда на мероприятие - Map\n'
                                'Запросить ссылку на викторину Kahoot - Kahoot\n'
                                'Запросить расписание мероприятия - Agenda\n'
                                'Задать вопрос спикерам на сцену - Question\n'
                                'Поучаствовать в голосовании - Vote\n'
                                'Запросить контакты ключевых представителей PwC - Contacts\n',
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: 'Map' in message.text)
def map(m):
    bot.send_message(m.chat.id, 'Please find a map!',
                        parse_mode='Markdown')

@bot.message_handler(func=lambda message: 'Kahoot' in message.text)
def kahoot(m):
    bot.send_message(m.chat.id, 'A link to Kahoot!',
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: 'Agenda' in message.text)
def agenda(m):
    bot.send_message(m.chat.id, 'Here is an agenda!',
                     parse_mode='Markdown')

#Эта часть обрабатывает сообщение, в котором есть текст "Question",
#То есть, когда пользователь нажимает на кнопку Question, либо может ввести это руками
@bot.message_handler(func=lambda message: 'Question' in message.text)
def question(m):
    msg = bot.send_message(m.chat.id, 'Please ask me a question!')
    #Бот отправляет сообщение и переходит к следующему хэндлеру
    bot.register_next_step_handler(msg, forward_question)
    
def forward_question(m):
    #Тут идет пересылка сообщения, которое отправил пользователь, и отправка пользователю сообщения, что оно было отправлено
    bot.forward_message('279790872',  m.chat.id, m.message_id)
    bot.send_message(m.chat.id, 'The question has been send. Thank you!')

@bot.message_handler(func=lambda message: 'Vote' in message.text)
def vote(m):
    bot.send_message(m.chat.id, 'Hey! Vote please!',
                     parse_mode='Markdown')

@bot.message_handler(func=lambda message: 'Contacts' in message.text)
def contacts(m):
    bot.send_message(m.chat.id, 'Our contacts...',
                     parse_mode='Markdown')

#bot.forward_message('92482885',  m.chat.id, m.message_id)

def main_loop():
    bot.polling(True)
    while 1:
        time.sleep(3)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)
