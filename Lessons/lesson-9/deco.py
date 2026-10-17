import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        print(f"Функция {func.__name__} отработала за: {elapsed:.6f} с.")
        return result
    return wrapper

@time_it
def sum_of_list(numbers: list) -> int:
    return sum(numbers)

@time_it
def min_of_list(numbers: list) -> int:
    return min(numbers)

my_numbers = list(range(1000))
print(sum_of_list(my_numbers))

# my_deco = time_it(sum_of_list)
# print(my_deco(my_numbers))

print(min_of_list(my_numbers))

