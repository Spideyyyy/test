import math

x = int(input("Введите число: "))
for i in range(0,x,2):
    if(i == 50):
        continue
    print(i)
    

s = 0
while s != x and s < x:
    print(s)
    s += 2

# a = int(input("Введите целое число: "))
# if(a % 2 == 1):
#     print("Число нечетное")
# elif(a % 2 == 0):
#     print("Число четное")

# # таблица умножения 

# n = int(input("Введите целое число: "))
# for i in range(1, 10):
#     print(f"{n} * {i} = {n * i}")

# sum = 0
# s = None
# while s != 0:
#     s = int(input("Введите число:" ))
#     if(s > 0):
#         sum += s
# print(f"Сумма положительных чисел = {sum}")














# print(100 // 46)
# # Задача 1
# a = int(input("Введите число: "))
# b = int(input("Введите число: "))
# print(f"Сумма: {a + b}")

# # Задача 2
# name = input("Введите ваше имя: ")
# age = int(input("Введите ваш возраст: "))
# print(f"Привет, {name}! Тебе {age} лет.")

# # Задача 3
# C = int(input("Введите температуру в градусах Цельсия: "))
# F = C * 9/5 + 32
# print(f"Температура в Фаренгейтах: {F}")
