# -*- encoding: utf-8 -*-
import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение параметров почты из файла .env
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
smtp_password = os.getenv("SMTP_PASSWORD")


# отправка сообщения
def send_email(email_text):
    server = smtplib.SMTP("smtp.yandex.ru", 587)
    server.starttls()
    server.login(sender_email, smtp_password)

    subject = "Death in 2023"

    message = MIMEText(email_text, _charset="utf-8")

    # меняем кодировку, чтобы не приходили кракозябры
    message["Content-Type"] = 'text/plain; charset="utf-8"'

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
