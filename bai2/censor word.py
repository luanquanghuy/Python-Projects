word = "Quang Huy"
result = []
print(word.split())
for i in word.split():
    if "HUY".lower() == i.lower():
        result.append("*" * len("HUY"))
    else:
        result.append(i)
print(" ".join(result))
print(word.count("u"))