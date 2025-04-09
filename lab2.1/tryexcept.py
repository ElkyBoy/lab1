# tryexcept.py

# Программа, которая запрашивает у пользователя число и обрабатывает ошибку
try:
    num = int(input("Введите число: "))
except ValueError:
    print("Ошибка! Это не число.")

# Программа, которая пытается открыть файл и обрабатывает ошибку
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Ошибка! Файл не найден.")