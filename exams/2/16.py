from sys import setrecursionlimit


def f(n):
    if n == 1: return 1
    elif n > 1: return n * f(n-1) - 1


def main():
    print(f(1000)/f(997))


if __name__ == '__main__': main()
