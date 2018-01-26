import facebook

acess_token = ''
with open('matruycap', 'r') as textfile:
    acess_token = textfile.readline()


print "'%s'" % acess_token