import check
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters

Token="376593798:AAHMNABESGpXiFGiQ8Bg-0CnHc2EwyXD1hk"
updater = Updater(token=Token)
dispatcher = updater.dispatcher

def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Bot çalışıyor hacı :D")
def hello(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id,text="Hello")
def echo(bot,update):
    if(check.url(update.message.text) != False):
        bot.sendMessage(chat_id=update.message.chat_id, text="Databaseye kaydettim")
    elif(update.message.text=="Hello"):
        bot.sendMessage(chat_id=update.message.chat_id, text="Sanada Hello")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text="Boş Konuşma "+update.message.from_user.first_name)


#---------------HANDLER IS HERE--------------------

start_handler = CommandHandler('start', start)
hello_handler=CommandHandler('hello',hello)
echo_handler = MessageHandler(Filters.text, echo)

#--------------------------------------------------
#----------------DISPATCHER IS HERE----------------

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)

#--------------------------------------------------

updater.start_polling()