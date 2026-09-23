post_title = "Питоны крутые змеи"
post_text = "Питоны зеленые и это уже круто."
is_published = True
is_draft = False

print(f"Пост: {post_title}")

guest_age = int(input("Введите ваш возраст: "))
is_adult_only = True
is_allow_view =  True

if is_adult_only:
    # print("доступ разрешен :)" if guest_age >= 18 else "доступ запрещен :(")
    if guest_age >= 18:
        print("доступ разрешен :)")
    else:
        print("доступ запрещен :(")
        is_allow_view = False
else:
    print("ограничений нет :)")

if is_allow_view:
    if is_published and not is_draft:
        print(f"Текст: {post_text}")
    elif is_draft:
        print("Статья в чернровике.")
    else:
        print("Пост скрыт.")


