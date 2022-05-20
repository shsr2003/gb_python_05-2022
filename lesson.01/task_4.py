"""
Задание 4.

Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и только арифметические операции.
Не используйте взятие по индексу.
"""

number = int(input("Ведите целое положительное число: "))

max_number = 0

while number > 0:
    iteration = number % 10
    if iteration >= max_number: max_number = iteration
    number = number // 10

print(f"Самая большая цифра в числе: {max_number}")
