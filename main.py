import os

import smtplib
from dotenv import load_dotenv

load_dotenv()


def send_email(message):
    sender = 'rostyamudrik@gmail.com'
    password = os.getenv('EMAIL_PASSWORD')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        server.sendmail(sender, sender, message)

        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password please!'


def main():
    message = input('Type your message: ')
    print(send_email(message=message))


if __name__ == '__main__':
    main()
