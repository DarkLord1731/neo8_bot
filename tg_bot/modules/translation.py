from googletrans import Translator

from telegram import Update, Bot
from telegram.ext import CommandHandler

from tg_bot import dispatcher

def translate(bot: Bot, update: Update):
    if update.effective_message.reply_to_message:
        msg = update.effective_message.reply_to_message
		
        args = update.effective_message.text.split(None, 1)
        language = args[1]
		
        translator = Translator()
        translation = translator.translate(msg.text, language)

        update.effective_message.reply_text(translation.text)


__help__ = """
 - /t: translates the message into English using Google Translate API. Additionally you could specify the language code to translate the message into (default=en).
Supported [language codes](https://cloud.google.com/translate/docs/languages)
"""

__mod_name__ = "Translator"


TRANSLATE_HANDLER = CommandHandler('t', translate)

dispatcher.add_handler(TRANSLATE_HANDLER)