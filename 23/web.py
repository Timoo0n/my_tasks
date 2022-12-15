def f(cur, end):
    if cur > end or cur == 14: return 0
    elif cur == end: return 1
    return f(cur+1, end)+f(cur+3, end)


print(f(2, 9)*f(9, 18))
