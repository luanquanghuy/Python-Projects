print(0b1, 0b10, 0b11, 0b100, 0b101, 0b111)
print(0b1 + 0b11)
print(0b11 *0b11)

print(bin(10))

print(int("0b100", 2))


shift_left = 0b1
shift_right = 0b110
shift_left <<= 2
shift_right >>= 2
print(bin(shift_left))
print(bin(shift_right))
