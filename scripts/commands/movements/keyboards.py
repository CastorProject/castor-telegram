#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def movements_keyboard():
    keyboardStr = [
        ['👋', 'Me alegro', 'Como estás', 'Muy bien'],
        ['¿Color?', '¿Animal?', 'También', '¿Ojos?', '¿Nariz?'],
        ['¿Jugar?', 'Adivina', 'Sigue intentando', 'Felicitar'],
        ['Despedida', '🙋‍♂️', '🙋', 'Boton'],
        ['◀️ Atrás']
    ]
    callbackStr = [
        ['greet', 'nicetomeet', 'howru', 'fine'],
        ['color', 'animal', 'metoo', 'eyes', 'nose'],
        ['wantplay', 'guess',  'tryagain', 'nice'],
        ['byeL', 'byeB', 'byeG', 'button'],
        ['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
