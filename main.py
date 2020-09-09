import telebot
from email.mime.multipart import MIMEMultipart
import smtplib as root
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

bot = telebot.TeleBot('1278073723:AAFp3-eHtuTBNJAHH4w07VzHkJHDPl7ApFU')

@bot.message_handler(commands=['start'])
def welcome(message):
    # данные пользователя
    name = message.from_user.first_name
    name1 = message.from_user.last_name
    url = message.from_user.username
    iduser = message.from_user.id
    # /данные пользователя
    print("------------------------\n" + "Имя: " + str(name) + " " + str(name1) + "\nСсылка: @" + str(url) + "\nID: " + str(iduser) + "\n------------------------")
    bot.send_message(message.chat.id, "✅Привет, я <i>бот для спама</i>, мой создатель - <a href='https://t.me/vsevolodhtmlru'>Всеволод html</a>, всё что надо, это написать почту, и спам уже в пути!\n/help для помощи😉", parse_mode='html')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Инструкция:\nДля спама введите /spam 'почта без кавычек'\nИ начнётся спам из 10 сообщений, больше доступно будет при покупке VIP")

@bot.message_handler(commands=['vip'])
def help(message):
    bot.send_message(message.chat.id, "Переведи <a href='https://yasobe.ru/na/sptg123'>сюда</a> деньги, и кидай скрин мне, @vsevolodhtml😎", parse_mode='html')


@bot.message_handler(commands=['spam'])
def mail(message):
    try:
        i = 0
        message.text = message.text.replace('/spam ', '')
        print(message.text)
        b = message.text
        if b == '/spam':
            bot.send_message(message.chat.id, 'Вы не ввели почту на которую полетит спам =)\n/help если что-то не понятно🤔')
            b = "vsevolodhtml@yandex.ru"
            i = 10
        else:
            bot.send_message(message.chat.id, 'Спам из 10 сообщений начат😎, купите /vip для бесконечного спама!')
        while i < 10:
            url = 'smtp.mail.ru'
            toaddr = b
            login = 'spam.bot.tg@bk.ru'
            password = 'sptg123123'
            message = 'КУКУ'
            msg = MIMEMultipart()
            msg['Subject'] = 'sptg'
            msg['From'] = login
            body = message
            msg.attach(MIMEText(body, 'plain'))
            server = root.SMTP_SSL(url, 465)
            server.login(login, password)
            server.sendmail(login, toaddr, msg.as_string())
            print('OK')
            i = i + 1
            time.sleep(1)
    except BaseException:
        bot.send_message(message.chat.id, '🚫ERROR🚫, /help для помощи🤔')

@bot.message_handler(content_types=['text'])
def text(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, '🚫ERROR🚫, /help вам в помощь, ибо я не знаю что вы сказали')
    
bot.polling(none_stop=True)
