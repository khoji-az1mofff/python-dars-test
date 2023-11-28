from transliterate import to_cyrillic,to_latin 
import telebot 
TOKEN='6711812302:AAEys-6tLAjO_QmNR7i49xdt_6PBRHg279k'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu alaykum, Hush kelibsiz! Ozodbek aka ") 
bot.infinity_polling()







# matn=input("Matin kiriting: ")
# print(f"{to_cyrillic(matn)}")