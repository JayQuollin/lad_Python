name = input("приветствую! как тя звать? ")

age = int(input("сколько тебе лет?"))

next_year_age = age + 1

print(f"Привет, {name}, в следующем году тебе будет {next_year_age}")
print("Привет, {0}, в следующем году тебе будет {1}".format(name,next_year_age))

next_year_string = "Привет, {name}, в следующем году тебе будет {age}"

print(next_year_string.format(name=name,age=next_year_age))


