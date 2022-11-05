def notation_from_10(num, notation_number=2):

    my_list = list()
    while num > 0:
        my_list = [num % notation_number] + my_list

        num //= notation_number

    return my_list


