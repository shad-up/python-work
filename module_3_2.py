def  send_email(message, recipient, *, sender = "university.help@gmail.com"):
    Valid = bool
    if '@' in recipient and '@' in sender:
        if '.com' in recipient or '.ru' in recipient or '.net' in recipient:
            if '.com' in sender or '.ru' in sender or '.net' in sender:
                Valid = True
            else: Valid = False
        else: Valid = False
    else: Valid = False
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    else:
        if Valid and sender != "university.help@gmail.com":
            print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса: ", sender, "на адрес: ", recipient)
        else:
            if Valid:
                print("Письмо успешно отправлено с адреса: ", sender, "на адрес: ", recipient)
            else: print("Невозможно отправить письмо с адреса: ", sender, "на адрес: ", recipient)
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')