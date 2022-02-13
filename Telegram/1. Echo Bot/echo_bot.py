import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    stick = open('Stickers/hello.webp', 'rb')
    bot.send_sticker(message.chat.id, stick)
    bot.send_message(message.chat.id,
                     'Приветствую тебя, {0.first_name} \nМеня зовут - <b>{1.first_name}</b>. Бот, призваный быть твоим '
                     'эхом.'.format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def resending(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
