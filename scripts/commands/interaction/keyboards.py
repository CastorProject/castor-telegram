#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.create_keyboard import createKeyboard

def interaction_keyboard():
    keyboardStr = [
        ['Esta es mi cabeza', 'Estos son mi ojos', 'Esta es mi nariz', 'Esta es mi boca'],
        ['¿Dónde está mi cabeza?', '¿Dónde están mis ojos?', '¿Dónde está mi nariz?', '¿Dónde está mi boca?'],
	['¿Dónde está tu cabeza?', '¿Dónde están tus ojos?', '¿Dónde está tu nariz?', '¿Dónde está tu boca?'],
	['Toquemos nuestra cabeza', 'Toquemos nuestros ojos', 'Toquemos nuestra nariz', 'Toquemos nuestra boca'],
	['Jugar', 'Juguemos a', 'Intenta otra vez', 'Bien hecho'],
        ['◀️ Atrás']
    ]
    callbackStr = [
	['myHead', 'myEyes', 'myNose', 'myMouth'],
	['wheresMyHead', 'wheresMyEyes', 'wheresMyNose', 'wheresMyMouth'],
	['wheresUHead', 'wheresUEyes', 'wheresUNose', 'wheresUMouth'],
	['pointHead', 'pointEyes', 'pointNose', 'pointMouth'],
	['play', 'play', 'tryagain', 'nice'],
	['back']
    ]
    return createKeyboard(keyboardStr, "inline", callbackStr)
