#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread

#ROS Libraries
import rospy
from std_msgs.msg import String

#Telegram Libraries
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton as Button

#Telegram logging
import logging

logging.basicConfig(format='%(asctime)s - %(name)30s - %(levelname)8s [%(funcName)s] %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class CastorECIBot():
    def __init__(self, name):
        self.name = name
        #Call of Initializer Functions
        self.initNode()
        self.initParameters()
        self.initSubscribers()
        self.initPublishers()
        self.initVariables()
        self.main_ros()
        #self.rospy.spin()
        #Call of main loop is done by Threads

    def initNode(self):
        self.rospy = rospy
        self.rospy.init_node(self.name, anonymous = False)
        self.rospy.loginfo("[%s] Starting", self.name)
        return

    def initParameters(self):
        ## TODO: Hide the Token, it can be used by anyone to control the bot!
        self.token = self.rospy.get_param('/token', '946333850:AAH859ChF-9jlIumuqWsIgXmQ6MMxCuBFTM')
        if self.token is None:
            self.rospy.logerr("No token found in /telegram/token param server.")
            exit(0)
        else:
            self.rospy.loginfo("Got telegram bot token from param server.")
        self.emotionsTopic = self.rospy.get_param('/emotions_topic', '/emotions')
        return

    def initSubscribers(self):
        return

    def initPublishers(self):
        self.pubEmotions = self.rospy.Publisher(self.emotionsTopic, String, queue_size = 5)
        return

    def initVariables(self):
        self.selected_function = False
        return

    def createKeyboard(self, strKeys):
        keyboard = []
        for row in strKeys:
            newRow = map(Button, row)
            keyboard.append(newRow)
        return keyboard

    #@send_typing_action
    def start(self, update, context):
        keyboardStr = [
            ['Emotions'],
            ['Teleop']
        ]
        keyboard = self.createKeyboard(keyboardStr)
        reply_markup = ReplyKeyboardMarkup(keyboard)
        message = (
            "🇨🇴 Hola! Yo soy CastorBot! \n"
    		"Estas son mis funcionalidades: \n\n"
    		"*Emotions* - Controla las emociones de Castor\n\n"
    		"Intenta ahora!"
    	)
        update.message.reply_text(
            message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
        return

    #@send_typing_action
    def emotions(self, update, context):
        keyboardStr = [
            ['Happy 😄', 'Sad 🙁'],
            ['Surprise 😲', 'Talk 🗣️'],
            ["◀️ Back"]
        ]
        keyboard = self.createKeyboard(keyboardStr)
        reply_markup = ReplyKeyboardMarkup(keyboard)
        message = (
            "Selecciona una emoción!"
        )
        update.message.reply_text(
            message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
        return

    def menu(self, update, context):
        keyboardStr = [
            ['Emotions'],
            ['Teleop']
        ]
        keyboard = self.createKeyboard(keyboardStr)
        reply_markup = ReplyKeyboardMarkup(keyboard)
        message = (
            "🤖 Estas son mis funcionalides 🤖\n",
            "Selecciona una!"
    	)
        update.message.reply_text(
            message,
            reply_markup = reply_markup,
            parse_mode = 'markdown'
        )
        return

    def textCallback(self, update, context):
        text = update.message.text
        if self.selected_function == True:
            print(text)
            ros_msg = None
            if text == u'Happy 😄':
                ros_msg = "happy"
            elif text == u'Sad 🙁':
                ros_msg = "sad"
            elif text == u'Surprise 😲':
                ros_msg = "surprise"
            elif text == u'Talk 🗣️':
                ros_msg = "talk"
            elif text == u'◀️ Back':
                self.selected_function = False
                self.menu(update, context)
            else:
                pass
            if ros_msg != None:
                self.pubEmotions.publish(ros_msg)
                self.emotions(update, context)
        else:
            if text == 'Emotions':
                self.emotions(update, context)
                self.selected_function = True
            else:
                self.selected_function = False
        return

    def error(self):
        logger.warn('Update "%s" caused error "%s"' % (update, error))
        self.rospy.warn('[%s] Error in telegram bot!', self.name)
        return

    def main_ros(self):
        self.rospy.loginfo("[%s] ROS interfacer for Telegram bot OK", self.name)
        self.main_bot()
        self.rospy.spin()

    def main_bot(self):
        updater = Updater(self.token, use_context = True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(MessageHandler(Filters.text, self.textCallback))
        dp.add_error_handler(self.error)

        updater.start_polling()
        logger.info('Listening humans as %s..' % updater.bot.username)
        self.rospy.loginfo('[%s] Telegram Updater for %s OK', updater.bot.username, self.name)
        updater.idle()
        self.main_ros()
        return

if __name__ == '__main__':
    try:
        Bot = CastorECIBot('telegram_bot')
    #Bot.main_bot()
    except:
        print("Something's gone wrong. Exiting")
