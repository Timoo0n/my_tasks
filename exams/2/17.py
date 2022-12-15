
def f():
    with open('17.txt', 'r') as file:
        my_list = list(map(int, file.read().strip().split('\n')))
        min_value = min(my_list)

        sum_list = []
        for i in range(len(my_list)-1):
            if abs(my_list[i]) % 117 == min_value or abs(my_list[i+1]) % 117 == min_value:
                sum_list += [my_list[i]+my_list[i+1]]
        print(len(sum_list), max(sum_list))
        

        

def main(): f()


if __name__ == '__main__': main()
