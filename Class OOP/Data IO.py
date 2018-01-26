with open("text1.txt", "w") as my_file:
    my_file.write("Quang Huy")

my_file1 = open("text2.txt", "w")
my_file1.write("Lop KTPM 16A")

if my_file.closed and my_file1.closed:
    print("true")
else:
    print('false')
