"""
Множества: уникальные значения. Дан список тегов tags (с дублями). Составьте множество уникальных тегов через set, затем:

проверьте, есть ли в нём конкретный тег через in;
добавьте новый тег через add;
удалите несуществующий тег через discard (без ошибки) и через remove в try/except — запишите, чем они отличаются, в комментарии.
"""

tags = ["love","photooftheday","happy","instagood","love","like4like","followme","cozy","love","followme", "cute"]

unic_tegs = set(tags)
print(unic_tegs)

print("happy" in unic_tegs)
print("sunset" in unic_tegs)

unic_tegs.add("sunset")

imposter_teg = "olololo"
unic_tegs.discard(imposter_teg)

try:
    unic_tegs.remove(imposter_teg)
except KeyError:
    print(f"Ошибка: тег {imposter_teg} не существует")