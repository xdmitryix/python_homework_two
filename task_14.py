# Задача 14: Про степени двойки

n = int(input('введи число N:'))
count = 0
if n <= 1:
    print('некорректный ввод !')
while 2**count < n:
     print(2**count)
     count+=1
