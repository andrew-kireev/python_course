import telebot
from telebot import apihelper



# REQUEST_KWARGS={
#     'proxy_url': 'socks5://112.74.13.143:1080',
#     # Optional, if you need authentication:
#     'urllib3_proxy_kwargs': {
#         'assert_hostname': 'False',
#         'cert_reqs': 'CERT_NONE'
#         # 'username': 'user',
#         # 'password': 'password'
#     }
# }
bot = telebot.TeleBot('1175450649:AAFWOtuJXr0XagU-HUPetmSTtUmDCQaGA_4')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        print('bolt')
