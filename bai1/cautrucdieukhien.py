# Cau truc if..elif..else
a = 5
if a > 5:
    print('a =', a, 'lon hon 5')
elif a < 5:
    print('a =', a, "nho hon 5")
else:
    print('a =', a)
# Python không có cấu trúc điều khiển switch..case
# Cau truc for..in
i = 0
arr = ['quang', 'huy', 5, 7]
for item in arr:
    print('item =', item)
for letter in 'Python':
    print('letter =', letter)
for i in range(1, 9):
    print(i)
# Cau truc while
n = 0
while n < 5:
    print('n =',n)
    n += 1
list = ['quang', 5.3, 'huy', 8]
print(list)
print(list[1:3])