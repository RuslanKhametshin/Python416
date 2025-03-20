import re

def validate_login(text):
    st = r"[a-zA-Z0-9а-яА-Я._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(st, text)
    return emails
text = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
result = validate_login(text)
print(text)
print(result)