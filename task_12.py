# Задача 12: Про Петю и Катю

s = int(input('сумма загаданных чисел S:'))
p = int(input('произведение загаданных чисел P:'))
x = 0
y = 0
if s < 0 or p < 0:
    print('некорректный ввод !')
else: 
    for i in range(1000):
        for j in range(1000):
            if (i + j == s) and (i * j == p):
                x = i
                y = j
                break
    print(f'загаданы числа {x} и {y}')
