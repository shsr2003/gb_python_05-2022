"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.
"""

number1 = int(input("Введите число: "))

s = str(number1)

number2 = s + s
number3 = s + s + s

sum0 = number1 + int(number2) + int(number3)

print(f"Сумма чисел: ", sum0)
