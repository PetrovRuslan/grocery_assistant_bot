import telebot

bot = telebot.TeleBot('1594398291:AAHnUCHrqZlzmlljp-SnpUFjo72Hqau2Tbc')

@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
    if message.text == "/start": 
        bot.send_message(message.from_user.id, "Привет, давай я расскажу тебе о том, зачем я нужен?") 
    elif message.text == "/help": 
        bot.send_message(message.from_user.id, "Напиши Привет") 
    else: 
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)