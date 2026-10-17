import time
import functools

def time_it(func):
    @functools.wraps(func) # декоратор для декоратора
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за: {elapsed:.6f} с.")
        return result
    return wrapper

def logged(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Вызов: {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"Результат: {func.__name__} == {result}")
        return result
    return wrapper


@logged
@time_it
def sum_of_list(numbers: list) -> int:
    return sum(numbers)

print(sum_of_list.__name__)

@logged
@time_it
def min_of_list(numbers: list) -> int:
    return min(numbers)

my_numbers = list(range(10))
print(sum_of_list(my_numbers))

# my_deco = time_it(sum_of_list)
# print(my_deco(my_numbers))

print(min_of_list(my_numbers))