title = "В мире животных"

print(title[4])
print(title[-2])
print(title[7:])
print(title[-8:])
print(title[2:6])
print(title[::-1])

print(title.upper())
print(title.lower())

dirty = "   жирафы  ! ."
clean = dirty.strip("!. ")
print(clean)
print(f"Длина до .strip: {len(dirty)}, после: {len(clean)}")

print(title.replace("животных", "роботов"))
print(title.replace("и", "ы"))

# empt_str = ""
# print(empt_str[0])

print(title.startswith("В"), title.endswith("животных"))

print(title.find("животных"))

print(title.count("и"))
