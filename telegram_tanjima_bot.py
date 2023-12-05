from transliterate import to_cyrillic,to_latin 
import telebot 
TOKEN='6711812302:AAEys-6tLAjO_QmNR7i49xdt_6PBRHg279k'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob= "Assalomu alaykum, Hush kelibsiz!"
    javob+="\nMatn kiriting:" 
    bot.reply_to(message,javob)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message, javob) 
bot.infinity_polling()







# matn=input("Matin kiriting: ")
# print(f"{to_cyrillic(matn)}")