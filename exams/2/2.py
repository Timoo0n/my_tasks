from itertools import product

def f():
    print('X Y W Z')
    for x, y, w, z in product(range(2), repeat=4):
        if not (((x <= z) <= y) or (not w)):
            print(x, y, w, z)


if __name__ == '__main__': f()
    
