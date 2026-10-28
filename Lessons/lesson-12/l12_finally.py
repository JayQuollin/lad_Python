import json
from pathlib import Path

POSTS_FILE = Path('posts.json')
def read_posts(path: Path) -> list:
    try:
        with path.open() as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файл отсутствует")
        data = []
    else:
        print(f"Файл {path} открыт, количество записей в файле {len(data)}")
    finally:
        print("Чтение файла завершено")
    return data

if __name__ == "__main__":
    read_posts = read_posts(POSTS_FILE)