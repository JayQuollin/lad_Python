def make_multyplier(multiplicator : int):
    def multiplier(number: int) -> int:
        return number * multiplicator
    return multiplier

double = make_multyplier(2)

print(double(10))
print(double(50))

triple = make_multyplier(3)
print(triple(10))
print(triple(50))

def make_counter(start: int = 0):
    count = start
    def increment(step: int = 1) -> int:
        nonlocal count
        count += step
        return count
    return increment


my_counter = make_counter()
print(my_counter())
print(my_counter(10))

print()
new_counter = make_counter(10)
print(new_counter(5))
print(my_counter())
