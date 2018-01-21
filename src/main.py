#!/usr/bin/env python3

import config as cfg
import telebot


bot = telebot.TeleBot(cfg.token)


@bot.message_handler(commands=["test"])
def command_test(msg):
    chat_id = msg.chat.id
    print("cmd>", msg.chat.id, ">", msg.text)
    msgTo = "I see command `test`"
    bot.send_message(chat_id, msgTo)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print(message.chat.id, ":", message.text)
    bot.send_message(message.chat.id, message.text)


def main():
    print("bot> start")
    bot.polling(none_stop=True)
    print("bot> end")


if __name__ == "__main__":
    main()
    exit(0)

