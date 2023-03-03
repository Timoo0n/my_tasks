value = 5*216**3031+4*36**3042-3*6**3053-3064
s = 0
while value:
    s += value % 6
    value //= 6
print(s)
