#!/usr/bin/python
# -*- coding: utf-8 -*-

from commands.emotions.callback import emotions_callback
from commands.movements.callback import movements_callback

from telegram import ReplyKeyboardRemove
from commands.emotions.keyboards import emotions_keyboard
from commands.movements.keyboards import movements_keyboard
from commands.start.keyboards  import start_keyboard

command_callback = {'emotions': emotions_callback, 'movements': movements_callback}

def callback_handler(update, context, pubEmotions, pubMovements):
    publishers = {'emotions': pubEmotions, 'movements': pubMovements}
    chat_data = context.chat_data
    print(context)
    print(chat_data)
    if not context:
	query.answer(text="")
        query.edit_message_text(text="Selecciona una opción en el teclado:")
	return
    #Get update data
    query = update.callback_query
    callback_function = command_callback[chat_data["command"]]
    publisher = publishers[chat_data["command"]]
    handled_response = callback_function(update, context, publisher)
    #Check callback callback_data
    if chat_data['command'] == "emotions":
        #Notify Telegram that we have answered
        query.answer(text="")
        #Update answer
        keyboard = emotions_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = (
            "Selecciona una emoción!"
        )
        query.edit_message_text(
            text=message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
    elif chat_data['command'] == "movements":
        #Notify Telegram that we have answered
        query.answer(text="")
        #Update answer
        keyboard = movements_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)
        message = (
            "Selecciona una opción en el teclado:"
        )
        query.edit_message_text(
            text=message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
    else:
        #Notify Telegram that we have answered
        query.answer(text="")
        query.edit_message_text(text="Selecciona una opción en el teclado:")
    return
