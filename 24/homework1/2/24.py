with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    print(s.count('TIK')+s.count('TOK'))
