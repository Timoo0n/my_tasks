
for x in range(21):
    for y in range(21):
        v = (10+x*21+y*21**2+2*21**3+3*21**4) + (8+21+y*21**2+6*21**3+21**4)
        if v % 12 == 0 and y % 2 == 1:
            if y == 7:
                print(x, v // 12)
