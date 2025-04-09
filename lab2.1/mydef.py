# mydef.py

# Функция, которая принимает два числа и возвращает их сумму
def add(a, b):
    return a + b

print(f"Сумма: {add(2, 3)}")

# Функция, которая проверяет, является ли число простым
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(f"Число 7 простое? {is_prime(7)}")

# Функция, которая принимает список чисел и возвращает их среднее значение
def average(numbers):
    return sum(numbers) / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(f"Среднее значение: {average(numbers)}")