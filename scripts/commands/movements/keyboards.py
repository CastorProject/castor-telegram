#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def movements_keyboard():
    keyboardStr = [
        ['Saludo', 'Me alegro', 'Como estás', 'Muy bien'],
        ['¿Color?', '¿Animal?', 'También'],
        ['¿Jugar?', 'Adivina', 'Sigue intentando', 'Felicitar'],
        ['Despedida', 'ChaoO', 'ChaoA'],
        ['◀️ Atrás']
    ]
    callbackStr = [
        ['greet', 'nicetomeet', 'howru', 'fine'],
        ['color', 'animal', 'metoo'],
        ['wantplay', 'guess',  'tryagain', 'nice'],
        ['byeL', 'byeB', 'byeG'],
        ['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
