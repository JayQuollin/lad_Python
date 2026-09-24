
login = "Kemeron"
password = "1234"
age = 27
email = "azaza@mail.ru"


login_error = False
password_error = False
age_error = False
email_error = False

"""
Можно ли считать замыканием - выход через определенный if и пропуск остальных веток?
"""
if not login:
    login_error = True
    print("Ошибка: пустой логин")
elif len(password) < 7:
    password_error = True
    print("Ошибка: пароль слишком короткий")
elif age < 18:
    age_error = True
    print("Ошибка: запрещено для детей")
elif not ("@" in email):
    email_error = True
    print("Ошибка: некорректный эмэил")

"""
Замыкание на or: первый True и вас выгнали
"""
if login_error or password_error or age_error or email_error:
    print("В доступе отказано")
else:
    print("С возвращением!")