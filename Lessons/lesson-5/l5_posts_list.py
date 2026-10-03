posts = [
    ["2026-02-10", "Как установить uv", "Инструментарий"],
    ["2026-02-14", "Списки в Python", "Python"],
    ["2026-02-18", "Введение в Django", "Django"],
]

print("Добро пожаловать в блог CLI")

while True:
    print(
        """
        Что делаем?
        1 - добавить пост
        2 - Показать все посты
        3 - Отсортировать по дате
        4 - Отфильтровать по категории
        0 - Выйти
        """
    )

    choice = input("Ваш выбор: ")
    if choice == "1":
        new_date = input("Введите дату форматом yyyy-mm-dd: ")
        new_title = input("Введите заголовок: ")
        new_category = input("Введите категорию: ")
        posts.append([new_date, new_title, new_category])
        print(f"Пост \"{new_title}\" добавлен")

    elif choice == "2":
        print("\nВсе посты:")
        for post in posts:
            print(f"{post[0]} - {post[1]} - {post[2]}")

    elif choice == "3":
        posts.sort()
        print(f"Отсортировано по дате:")
        for post in posts:
            print(f"{post[0]} - {post[1]} - {post[2]}")
    elif choice == "4":
        target = input("Придется ввести категорию: ")
        filtered = [post for post in posts if post[2] == target]
        if filtered:
            for post in filtered:
                print(f"{post[0]} - {post[1]} - {post[2]}")
        else:
            print("Посты не найдены")
    elif choice == "0":
        print("До скорой встречи!")
        break
    else:
        print("непонял")