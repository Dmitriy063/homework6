# Напишите программу, которая принимает на вход число N и выдает набор квадратов чисел от 1 до N.
n = int(input('Введите число: '))
lst = list(i for i in range(1,n+1))
print(lst)
lst = list(map(lambda i: i * i, lst))
print(lst)