class ValidationError(Exception):
    """Ошибка валидации данных"""

def create_post(title: str, body: str) -> dict:
    if not title.strip():
        raise ValidationError("Заголовок не должен быть пустым")
    if not body.strip() or len(body) < 15:
        raise ValidationError("Текст поста не должен быть меньше 15 символов")

    return {
        "title": title,
        "body": body
    }

if __name__ == "__main__":

    title = "R2D2"
    body = "Звездные войны рулят!!"


    try:
        print(create_post(title, ""))
    except ValidationError as e:
        print(f"Не удалось создать пост, ошибка: {e}")
