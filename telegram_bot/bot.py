from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json

updater = Updater(token='Токет от Telegram')
dispatcher = updater.dispatcher

def startCommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Эй, приветики! :)')

def textMessage(bot, update):
    request = apiai.ApiAI('Токен от ИИ').text_request()
    request.lang = 'ru'
    request.session_id = 'Bot_for_me'
    request.query = update.message.text
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech']
    if response:
        bot.send_message(chat_id=update.message.chat_id, text=response)
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Я тебя не понял...')

start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)

updater.idle()


