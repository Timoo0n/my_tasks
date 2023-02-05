with open('26.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    my_stock = sorted([int(i) for i in file])  # Склад
    cells = []  # Ячейки

    while my_stock:  # Пока на складе есть контейнеры
        block = []  # Блок
        value = my_stock[0]  # Предыдущее значение для сравнения
        block += [value]
        for i in range(1, len(my_stock)):  # Скидываю в блок все нужные контейнеры
            if my_stock[i]-value >= 7: block += [my_stock[i]]; value = my_stock[i]
        for j in block:  # Удаляю со склада все контейнеры, которые подходят
            my_stock.remove(j)
        cells.append(block)  # Добавляю в ячейку блок
    print(len(cells), max(len(i) for i in cells))
                
                
        
    
