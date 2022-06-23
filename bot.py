from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters,CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup


button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)
def start(update: Update, context: CallbackContext):
    id = update.effective_user.id
    f_name = update.effective_user.first_name
    l_name = update.effective_user.last_name
    username = update.effective_user.username



    update.message.reply_text(f"your ID:  {update._effective_user.id}\ncurrent chat ID:  {update.message.chat_id}",reply_markup=button)
    return 'bot'



conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
                  ],
    states={
        'bot': [

            MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
            MessageHandler(Filters.all, start),
        ],
    },
fallbacks = [
MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
    CommandHandler('start', start)
]

)







updater = Updater("5350123992:AAFQ5IGMFnWQLYuraUeZ0XtKmL7R5hoQjjs")
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()


