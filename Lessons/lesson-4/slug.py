def build_slug(title: str) -> str:
    result = title.lower()
    result = result.replace(" ", "-")

    clean = []
    for char in result:
        if char.isalnum() or char == "-":
            clean.append(char)
        else:
            clean.append("-")

    result = "".join(clean)

    while "--" in result:
        result = result.replace("--", "-")

    result = result.strip("-")
    return result


my_title = "Загибательная ***** арифметика    и пути её применения!!!"

print(my_title)
print(build_slug(my_title))

