# myfile.py

# Программа, которая создает текстовый файл и записывает в него строку
with open("example.txt", "w") as file:
    file.write("Hello, File!")

# Программа, которая читает содержимое файла и выводит его на экран
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Программа, которая добавляет новую строку в существующий файл
with open("example.txt", "a") as file:
    file.write("\nДобавляем еще одну строку.")