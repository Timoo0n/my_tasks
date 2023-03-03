from string import ascii_lowercase
# F = 15

for x in range(16):
    value = 0 + x*17 + 0*17**2 + 1*17**3 + 15 + 15*17 + x*17**2 + 0*17**3 + 15*17**4
    if value % 13 == 0:
        print(value // 13)
