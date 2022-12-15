from functools import lru_cache

def moves(x):
    my_list =[]
    if (x+1) <= 60: my_list += [x+1]
    elif (x+2) <= 60:my_list += [x+2]
    elif (x*2) <= 60: my_list += [x*2]
    return my_list


@lru_cache(None)
def f(h):
    if h >= 51: return 'w'
    elif any(f(i) == 'w' for i in moves(h)): return 'p1'
    elif all(f(i) == 'p1' for i in moves(h)): return 'v1'
    elif any(f(i) == 'v1' for i in moves(h)): return 'p2'
    elif all(f(i) == 'p1' or f(i) == 'p2' for i in moves(h)): return 'v2'
    #elif any(f(i) == 'v2' for i in moves(h)): return 'p3'
    #elif all(f(i) == 'p1' or f(i) == 'p2' or f(i) == 'p3' for i in moves(h)): return 'v3'
    


if __name__ == '__main__':
    for i in range(1, 51):
        result = f(i)
        if result == 'v2':
            print(i, result)
    
