import random

a = random.randrange(100)
lst = []
for i in range(100):
    while a in lst:
        a = random.randint(1, 100)
    lst.append(a)

print(lst)
lst.sort()
print(lst)
print(random.sample(lst, 3))
print(random.betavariate)
