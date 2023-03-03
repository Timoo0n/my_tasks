def f(c, e, a):
    if c > e: return 0
    if c == e: return 1

    if a == "*2":
        return f(c+1, e, "+1") + f(c+2, e, "+2")
    else:
         return f(c+1, e, "+1") + f(c+2, e, "+2") + f(c*2, e,"*2")

print(f(1, 15, ""))
