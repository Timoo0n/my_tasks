value = 6*512**180+7*64**181+3*8**184+5*8**125-65
l = []
while value:
    l = l + [value % 64]
    value //= 64
print(l.count(0))
