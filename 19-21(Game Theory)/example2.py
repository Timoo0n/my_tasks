from functools import lru_cache


def moves(h):
    a, b = h
    return (a+1, b), (a, b+1), (a*2, b), (a, b*2)


@lru_cache(None)
def f(h):
    if sum(h) >= 74:
        return 'END'
    elif any(f(x) == 'END' for x in moves(h)):
        return '�1'
    elif all(f(x) == '�1' for x in moves(h)):
        return '�1'
    elif any(f(x) == '�1' for x in moves(h)):
        return '�2'
    elif all(f(x) == '�1' or f(x) == '�2' for x in moves(h)):
        return '�2'


if __name__ == '__main__':
    print(f(11))