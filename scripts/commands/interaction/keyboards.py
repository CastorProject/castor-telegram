#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def interaction_keyboard():
    keyboardStr = [
        ['¿Jugar?', 'Juguemos'],
	['Mi cabeza', 'Mis ojos', 'Mi nariz', 'Mi boca'],
        ['¿Mi cabeza?', 'Mis ojos?', '¿Mi nariz?', '¿Mi boca?'],
	['¿Tu cabeza?', '¿Tus ojos?', '¿Tu nariz?', '¿Tu boca?'],
	['Tocar cabeza', 'Tocar ojos', 'Tocar nariz', 'Tocar boca'],
	['Intenta otra vez', 'Bien hecho', 'Gracias'],
	[ 'Despedida', '🙋‍♂️', '🙋'],
        ['◀️ Atrás']
    ]
    callbackStr = [
	['wantplay', 'play'],
	['myHead', 'myEyes', 'myNose', 'myMouth'],
	['wheresMyHead', 'wheresMyEyes', 'wheresMyNose', 'wheresMyMouth'],
	['wheresUHead', 'wheresUEyes', 'wheresUNose', 'wheresUMouth'],
	['pointHead', 'pointEyes', 'pointNose', 'pointMouth'],
	['tryagain', 'nice', 'thanku'],
	['byeL', 'byeB', 'byeG'],
	['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
