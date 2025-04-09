# mydict.py

# Программа, которая создает словарь с информацией о студенте
student = {
    "name": "Иван",
    "age": 20,
    "course": 3
}
print(student)

# Программа, которая объединяет два словаря
dict1 = {"name": "Иван", "age": 20}
dict2 = {"course": 3, "university": "МГУ"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Программа, которая проверяет, есть ли определенный ключ в словаре
key = input("Введите ключ для проверки: ")
if key in student:
    print(f"Ключ '{key}' есть в словаре.")
else:
    print(f"Ключ '{key}' нет в словаре.")