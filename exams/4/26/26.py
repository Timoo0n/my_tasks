with open('26.txt', 'r') as file:
    n = int(file.readline())
    shop = []
    for values in file:
        value, color = values.split()
        shop += [[int(value), color]]
    shop = sorted(shop, key=lambda el: el[0])
        
    presents = []

    while shop:
        block = []
        value, color = shop[0]
        block += [[value, color]]
        for i in range(len(shop)):
            new_value, new_color = shop[i]
            if new_color != color and new_value - value >= 7:
                block += [[new_value, new_color]]
                color, value = new_color, new_value
        for present in block:
            shop.remove(present)
        presents.append(block)
    print([len(i) for i in presents])  # короч нужен перебор, так как жадный штука не работает
            
        
    
