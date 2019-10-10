#!/usr/bin/python
# -*- coding: utf-8 -*-

from telegram import InlineKeyboardMarkup, ReplyKeyboardRemove
from commands.interaction.keyboards import interaction_keyboard

def interaction(update, context):
    context.chat_data["command"] = "interaction"
    keyboard = interaction_keyboard()
    reply_markup = InlineKeyboardMarkup(keyboard)
    message = (
        "Selecciona una emoción!"
    )
    update.message.reply_text(
        message,
        reply_markup = reply_markup,
        parse_mode = 'markdown'
    )
    return
