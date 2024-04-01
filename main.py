
import telebot
bot = telebot.TeleBot('ваш токен')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Введите текст с смайликами и этих смайликов не будет')

@bot.message_handler(content_types=['text'])
def menu(message):
    smails = message.text
    bot.send_message(message.chat.id, smails.translate({ord(i): None for i in '👋🤫😐😂😘❤️😍😊💋😝😌🙊😚😅😅😏😡😱😒😳😜🙈😉😃😢😭😄😔☺️🤔😁'}))


bot.polling(none_stop=True)

# s = input()
#
# print(s.translate({ord(i): None for i in '👋🤫😐😂😘❤️😍😊💋😝😌🙊😚😅😅😏😡😱😒😳😜🙈😉😃😢😭😄😔☺️👍🤔😁'}))