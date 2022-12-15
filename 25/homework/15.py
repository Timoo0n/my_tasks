
def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    for i in range(10332, 12356+1):
        r = div(i**2)
        if len(r) == 3:
            print(i**2, max(r))

main()
