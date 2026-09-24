
print("bool(0) ==", bool(0), "- это целочисленное ничто")
print('bool(0.0) ==', bool(0.0), "- это численное ничто")
print('bool("") ==', bool(""), "- это пустая строка")
print('bool("0") ==', bool("0"), "- это не пустая строка")
print("bool([]) ==", bool([]), "- это пустой массив")
print("bool([1]) ==", bool([1]), "- это не пустой массив")
print("bool(None) ==", bool(None), "- это ничто")
print("bool(False) ==", bool(False), "- это False")


# ошибочная проверка существования переменной массива:
fruits = []
if fruits:
    fruits.append("bananas")

print("Фрукты, которые мы привезли:", fruits)
