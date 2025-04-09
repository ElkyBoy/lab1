# calc.py
def calculator():
    print("Добро пожаловать в калькулятор!")
    while True:
        try:
            expression = input("Введите выражение (или 'exit' для выхода): ")
            if expression.lower() == 'exit':
                print("До свидания!")
                break
            # Пробуем вычислить выражение
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}. Попробуйте еще раз.")
            
if __name__ == "__main__":
    calculator()