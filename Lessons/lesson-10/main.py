from blog import data, ui

def main() -> None:
    while True:
        print("""
        МЕНЮ
        1. Добавить статью
        2. Показать статьи
        0. Выход
        """)
        choice = input("> ")
        if choice == "1":
            ui.create_post_menu()
        elif choice == "2":
            ui.show_posts_menu()
        elif choice == "0":
            print("Выход . . .")
            return
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
