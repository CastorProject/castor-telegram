#!/usr/bin/python
# -*- coding: utf-8 -*-
from telegram import ReplyKeyboardRemove

from commands.interaction.keyboards import interaction_keyboard
from commands.start.keyboards  import start_keyboard

def interaction_callback(update, context, pubMovements):
    #Get update data
    query = update.callback_query
    #Check callback callback_data
    if query['data'] != "back":
        #Publish interaction in ROS
        pubMovements.publish(query["data"])
        #Notify Telegram that we have answered
        query.answer(text="")
        #Update answer
        keyboard = interaction_keyboard()
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
