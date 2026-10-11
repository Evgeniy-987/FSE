import string

password = input()

upper = string.ascii_uppercase
lower = string.ascii_lowercase
special = '*-#%Qwe'
allowed = upper + lower + string.digits + special

errors = []
if len(password) != 8:
    errors.append("Длина пароля не равна 8")
if not any(s in upper for s in password):
    errors.append("В пароле отсутствуют заглавные буквы")
if not any(s in lower for s in password):
    errors.append("В пароле отсутствуют строчные буквы")
if not any(s.isdigit() for s in password):
    errors.append("В пароле отсутствуют цифры")
if not any(s in special for s in password):
    errors.append("В пароле отсутствуют специальные символы")
if not all(s in allowed for s in password):
    errors.append("В пароле используются непредусмотренные символы")

if errors:
    print(*errors, sep="\n")
else:
    print("Надежный пароль")