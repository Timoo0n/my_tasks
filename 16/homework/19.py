
def f(n):
    if n <= 1: return n
    return n + f(n // 3) if n > 1 and n % 3 == 0 else n + f(n+3)


def main():
    for i in range(1, 1000):
        try:
            print(i, f(i))
        except: ...

main()
