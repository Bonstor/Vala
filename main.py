import config
import telebot
import time
import random

bot = telebot.TeleBot(config.token)
input_file = open("some.txt", "r")
answer_list = input_file.readlines()
input_file.close()
petyh_list = []


def new_answer(message):
    answer_list.append(message.text)
    bot.reply_to(message, 'Добавлено')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    # test
    #bot.send_message(254247271, message.from_user.first_name)
    #bot.send_message(254247271, '********************\n')
    print(message.from_user)
    print(message.text)
    print('***********************\n')

    if (message.from_user.username in petyh_list) or (message.from_user.id in petyh_list):
        menu = int(random.random() * len(answer_list))
        answer = answer_list.pop(menu)
        answer_list.append(answer)
        bot.reply_to(message, answer)
        return 0

    if message.text.startswith('/добавь '):
        ans = message.text
        ans = ans.replace('/добавь ', '').capitalize()
        bot.send_message(message.chat.id, "Добавленно " + ans)
        answer_list.append(ans)
        output_file = open("some.txt", "a")
        output_file.write(ans + '\n')
        output_file.close()
        return 0

    if (message.text.startswith('/петух ')) and (message.from_user.id == 234672324):
        ans = message.text
        ans = ans.replace('/петух ', '')
        bot.send_message(message.chat.id, "Выслеживаю нового петушару!\n" + ans + " привет привет!")
        petyh_list.append(ans)
        return 0

    if message.text.startswith('/петух '):
        bot.send_message(message.chat.id, "Ах ты маленький засранец!!!\n" + message.from_user.first_name + " вздумал наебать меня?!?!?!")
        bot.send_message(message.chat.id, "Выслеживаю нового петушару!\n" + message.from_user.first_name + " привет привет!")
        petyh_list.append(message.from_user.id)
        return 0


def loop():
    try:
        bot.polling(none_stop=True)
    except Exception:
        print('Save me!')
        time.sleep(50)
        loop()

loop()
