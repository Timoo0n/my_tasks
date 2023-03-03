with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    print(s.count('BOSS')-s.count('JBOSSS')-s.count('JBOSSB')-s.count('JBOSSO')-s.count('OBOSSJ')-s.count('BBOSSJ')\
          -s.count('SBOSSJ')-s.count('JBOSSJ'))
