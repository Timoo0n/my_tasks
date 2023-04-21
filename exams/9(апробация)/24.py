with open('24_6757.txt', 'r', encoding='utf-8') as file:
    s = file.read().replace('CFE', '*').replace('FCE', '*').replace('C', ' ')\
        .replace('D', ' ').replace('F', ' ').replace('E', ' ')
    print(max(len(i) for i in s.split()))
     
