"""
Звёздочка (валидация телефона/email). Написать проверку корректности e-mail без регулярных выражений, только методами
строк:
- есть ровно один @,
- слева и справа от него есть непробельные символы,
- в доменной части есть точка,
- домен заканчивается на 2+ буквы (endswith + проверка isalpha на суффиксе).
Дополнительно — проверить номер телефона в формате +7-XXX-XXX-XX-XX: разбить по - на 5 частей, первая равна +7,
остальные — isdigit() и нужной длины (len). Вывести True/False для нескольких примеров.

"""

def is_it_valid(email):

    if not(email):
        return "EmptyError"

    dog_count = email.count('@')
    if dog_count != 1:
        return "DogsError"
    else:
        dog_pose = email.find('@')

    space_count= email.find(" @") + email.find("@ ")
    if space_count != -2:
        return "SpaceError"
        # Вообще я бы это место поменяла на отсутсвие пробелов в целом
        # Но делаю по тз заказчика :)

    domen = email[dog_pose:]
    if domen.count('.') == 0:
        return "DomenPointsError"
    else:
        domen_pose = domen.rfind('.')

    if len(domen[domen_pose:]) <= 2:
        return "DomenError"

    return True


this_string = "123@123.ru"
print(is_it_valid(this_string))
