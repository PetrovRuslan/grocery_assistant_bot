import telebot

bot = telebot.TeleBot('1594398291:AAHnUCHrqZlzmlljp-SnpUFjo72Hqau2Tbc')

# def start(bot, update):
#     update.message.reply_text("Привет! Я бот-повторюшка. Напишите мне что-нибудь!")

# @bot.message_handler(content_types=["text"])
# def default_test(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)

# @bot.message_handler(commands = ['get_info', 'info'])
# def get_user_info(message):
#     markup_inline = types.InlineKeyboardMarkup()
#     item_yes = types.InlineKeyboardButton(text = 'Да', callback_data = 'yes')
#     item_no = types.InlineKeyboardButton(text = 'Нет', callback_data = 'no')

#     markup_inline.add(item_yes, item_no)
#     bot.send_message(message.chat.id, "ey мужик", 
#         reply_markup = markup_inline
#     )

# @bot.callback_query_handler(func = lambda call: True)
# def 

# @bot.message_handler(content_types =['text'])
# def start_message(message):
#     if message.text == "/start": 
#         keyboard = telebot.types.ReplyKeyboardMarkup(True)
#         keyboard.row('Привет', 'Пока')
#         bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

# @bot.message_handler(content_types=['text']) 
# def get_text_messages(message): 
#     if message.text == "/start": 
#         bot.send_message(message.from_user.id, "Привет, давай я расскажу тебе о том, зачем я нужен?") 
#     elif message.text == "/help": 
#         bot.send_message(message.from_user.id, "Напиши Привет") 
#     else: 
#         bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

# @bot.message_handler(commands=['test'])
# def start_message(message):
#     markup = telebot.types.InlineKeyboardMarkup()
#     markup.add(telebot.types.InlineKeyboardButton(text='Три', callback_data=3))
#     markup.add(telebot.types.InlineKeyboardButton(text='Четыре', callback_data=4))
#     markup.add(telebot.types.InlineKeyboardButton(text='Пять', callback_data=5))
#     bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?", reply_markup=markup)

# @bot.callback_query_handler(func=lambda call: True)
# def query_handler(call):

#     bot.answer_callback_query(callback_query_id=call.id, text='Спасибо за честный ответ!')
#     answer = ''
#     if call.data == '3':
#         answer = 'Вы троечник!'
#     elif call.data == '4':
#         answer = 'Вы хорошист!'
#     elif call.data == '5':
#         answer = 'Вы отличник!'

#     bot.send_message(call.message.chat.id, answer)

@bot.message_handler(content_types =['text'])
def process_step(message):
    chat_id = message.chat.id
    if message.text=='Привет':
        # bot.send_message(call.message.chat.id, answer1)
         bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?")
    else:
        # bot.send_message(call.message.chat.id, answer2)
         bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе?2")


# @bot.message_handler(content_types =['text'])
# def start_message(message):
#     if message.text == "/start": 
#         keyboard = telebot.types.ReplyKeyboardMarkup(True)
#         keyboard.row('Привет', 'Пока')
#         msg = bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)
#         bot.register_next_step_handler(msg, process_step)

# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True)
#     markup.add('1', '2') #Имена кнопок
#     msg = bot.reply_to(message, 'Test text', reply_markup=markup)
#     bot.register_next_step_handler(msg, process_step)

bot.polling(none_stop=True, interval=10)