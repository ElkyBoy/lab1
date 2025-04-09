# mylist.py

# Программа, которая создает список из 5 чисел и выводит их сумму
numbers = [1, 2, 3, 4, 5]
print(f"Сумма чисел: {sum(numbers)}")

# Программа, которая находит максимальное число в списке
max_number = max(numbers)
print(f"Максимальное число: {max_number}")

# Программа, которая удаляет дубликаты из списка
numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Список без дубликатов: {unique_numbers}")