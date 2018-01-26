n = float(input("Nhap vao so can bieu dien: "))
s = 0
if n < 0:
    s = 1
    n = abs(n)

p_nguyen = int(n)
p_thap_phan = float('0.' + str(n).split('.')[1])
n1 = len(bin(p_nguyen)[2:]) - 1
n2 = n1 + 127

result = [str(s), bin(n2)[2:], bin(p_nguyen)[3:]]

list_thap_phan = []
huu_han = True
while p_thap_phan and huu_han:
    for num in list_thap_phan:
        if abs(p_thap_phan - num) < 0.000000001:
            huu_han = False
            break
    if huu_han:
        list_thap_phan.append(p_thap_phan)
        p_thap_phan *= 2
        result.append(str(int(p_thap_phan)))
        p_thap_phan -= int(p_thap_phan)
else:
    result = ''.join(result)

result += '0' * (32 - len(result))
result = result[0] + '.' + result[1:9] + '.' +result[-23:]
print(result)
