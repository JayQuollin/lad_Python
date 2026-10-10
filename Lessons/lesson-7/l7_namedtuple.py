from collections import namedtuple


Person = namedtuple("Person", ["name", "age", "city"])

Evg = Person("Evgeniy", 35, "NiNo")
Mama = Person(name="Katusha", age=23, city="North")

print(Evg.name)
print(Mama.age)
print(Evg)

print(Person._fields)

print(Evg._asdict())

Evg_nexst_year = Evg._replace(age=36)

print(Evg.age, Evg_nexst_year.age)