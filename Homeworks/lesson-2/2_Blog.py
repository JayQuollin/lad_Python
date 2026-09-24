"""пост виден, если он опубликован и (не премиум или у пользователя есть подписка)"""

# Данные поста:
is_published = True
is_premium = False
text = "Эта музыка будет вечной если я заменю батарейки"

# Данные пользователя:
name = "Alex"
is_subscription = False

if is_published and (not is_premium or is_subscription):
    if text:
        print(text)
    else:
        print("Пост не найден")
else:
    print("Отказано в доступе")
