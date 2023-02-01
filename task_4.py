# задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


k = int(input('введи число k: '))
if k <= 0:
    print('некорректный ввод')
elif k == 1:
    print('[1, 0, 1]')
else:
    numbers_plus = []
    numbers_minus = []
    numbers_zero = [0]
    numbers_result = []
    result_length = k * 2 + 1
    numbers_plus.append(1)
    numbers_plus.append(1)
    for i in range(2,k):
        numbers_plus.append(numbers_plus[i-1] + numbers_plus[i-2]) 
    for j in range(k):
        numbers_minus.append(numbers_plus[-j-1])
    for k in range(0,k,2):
        numbers_minus[k] = numbers_minus[k] * -1
    numbers_result = numbers_minus + numbers_zero + numbers_plus
    print(numbers_result)