# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Факториал
# 5! = 120

n = int(input('Введите число: '))
fact = 1

for i in range(1, n + 1):
     fact = fact * i
print(fact)