numbers = [1, 2, 3, 4, 5]
names = ['Quang', 'Huy', 'Luan']
print('nhap: ')
# index = int(input())
# print(type(index))
# print(numbers[1])
# try:
#     print('dung', numbers[index])
# except IndexError:
#     print('Nhap sai')
print(3 in numbers)
print(2 not in numbers)
print('huy' in names)
print('Huy' in names)

print(numbers[2:4])

del numbers[2]
print(numbers)

del numbers[1:3]
print(numbers)

print(numbers + names)

numbers.append(10)
print(numbers)

numbers.pop(2) #Lay phan tu cuoi cung ra khoi mang va tra ve gia tri phan tu cuoi cung do
print(numbers)
"""Day la multi-line comment"""
bo = True
bo = 3.14
print(str(bo))
str1 = "Quang"
str2 = "Huy"
print("Ten toi %s la %s" % (str1, str2))
from datetime import datetime
now = datetime.now()
print(now)
print(now.time())
choices = ['pizza', 'pasta', 'salad', 'nachos']
for index, item in enumerate(choices):
    print(index + 1, item)