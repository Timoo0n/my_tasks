with open('26.txt', 'r', encoding='utf-8') as file:
    my_stock = []  # Склад
    for i in file:
        value, color = i.split()
        my_stock += [[int(value), color]] 
    my_stock.sort()
    
    cells = []  # Ячейки
    while my_stock:
        value, color = my_stock[0]  # Начальные значения, по которым идет отбор следующих контейнеров
        block = []  # Блок
        block += [[value, color]]

        for i in range(1, len(my_stock)):
            new_value, new_color = my_stock[i]
            if new_value - value >= 7 and new_color != color:
                block += [[new_value, new_color]]
                value, color = new_value, new_color  # Обновление начальных значений

        for container in block: 
            my_stock.remove(container)

        cells += [block]

    print(max([len(block) for block in cells]), len(cells))
     
