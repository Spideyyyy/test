import math

def math_sum(a,b):
    print(f"Сумма чисел {a} и {b} равна {a + b}")
def math_sub(a,b,operation):
    print(f"Разность чисел {a} и {b} равна {a - b}")
def math_multi(a,b,operation):
    print(f"Произведение чисел {a} и {b} равна {a * b}")
def math_div(a,b,operation):
    if(b != 0):
            print(f"Деление чисел {a} и {b} равна {a / b}")
    else:
        print("На ноль делить нельзя")
def math_exp(a,b):
    print(f"Число {a} в степени {b} равна {a ** b}")

def math_oper(a,b,operation):
    if(operation == "1" or operation == "Сложение" ):
        math_sum(a,b)
    elif(operation == "2" or operation == "Вычетание" ):
        math_sub(a,b)
    elif(operation == "3" or operation == "Умножение" ):
        math_multi(a,b)
    elif(operation == "4" or operation == "Деление" ):
        math_div(a,b)
    elif(operation == "5" or operation == "Степень" ):
        math_exp(a,b)


exit_prog = "Да"
while exit_prog == "Да" or exit_prog == "да":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("""
    Какую операцию с двумя числами хотите сделать?
    1. Сложение
    2. Вычетание 
    3. Умножение 
    4. Деление   
    5. Степень             
    """)
    math_oper(a,b,operation)
    exit_prog = input("Хотите продолжить? Да/Нет ")











# x = int(input("Введите число: "))
# for i in range(0,x,2):
#     if(i == 50):
#         continue
#     print(i)
    

# s = 0
# while s != x and s < x:
#     print(s)
#     s += 2

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
