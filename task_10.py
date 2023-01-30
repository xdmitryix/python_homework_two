# Задача 10: Про монетки

import random
n = int(input('введи количество монеток: '))
if n < 0:
    print('некорректный ввод !')
else:    
    coins = []
    for i in range(n):
        coins.append(random.randint(0,1))
    print(coins)
    eagle_one = 0
    tail_zero = 0
    for i in range(n):
        if coins[i] == 1:
            eagle_one += 1
        else:
            tail_zero += 1
    result = 0
    if eagle_one == tail_zero:
        print('Нужно перевернуть' ,eagle_one , 'монет(ы)')
    else:
        if eagle_one > tail_zero:
            print('Нужно перевернуть' ,tail_zero , 'монет(ы)')
        else:
            print('Нужно перевернуть' ,eagle_one , 'монет(ы)')
