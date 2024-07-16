def check_email_addr(email_addr):
    em = email_addr.lower()
    if em.find('@') >= 0 and (em.endswith('.com') or em.endswith('.ru') or em.endswith('.net')):
        return False
    return True


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if check_email_addr(recipient) or check_email_addr(sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    if sender.lower() == recipient.lower():
        print('Нельзя отправить письмо самому себе!')
        return
    if sender.lower() == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
        return
    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
