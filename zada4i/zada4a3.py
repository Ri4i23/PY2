# Задана последовательность натуральных чисел, завершающаяся числом 0.
# Требуется определить значение второго по величине элемента в этой последовательности, то есть элемента, который будет наибольшим,
# если из последовательности удалить наибольший элемент.
# Пример:
# 1
# 7
# 9
# 0
# Вывод:
# 7

numbers = [1, 7, 9, 0]

maxNumber = numbers[0]
for i in numbers:
    if i > maxNumber:
        maxNumber = i

numbers.remove(maxNumber)

maxNumber = numbers[0]
for i in numbers:
    if i > maxNumber:
        maxNumber = i

print(f'Второй по величине элемент = {maxNumber}')