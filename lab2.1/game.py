# game.py
import random

def guess_number_game():
    print("Добро пожаловать в игру 'Угадай число'!")
    number_to_guess = random.randint(0, 10)  # Генерация случайного числа от 0 до 10
    attempts = 3  # Количество попыток
    
    while attempts > 0:
        try:
            user_guess = int(input(f"Угадайте число от 0 до 10. У вас {attempts} попыток: "))
            
            if user_guess < number_to_guess:
                print("Неверно! Загаданное число больше.")
            elif user_guess > number_to_guess:
                print("Неверно! Загаданное число меньше.")
            else:
                print("Поздравляем! Вы угадали число!")
                break
        except ValueError:
            print("Пожалуйста, введите число.")
        
        attempts -= 1
    
    if attempts == 0:
        print(f"К сожалению, вы не угадали число. Загаданное число было {number_to_guess}.")

if __name__ == "__main__":
    guess_number_game()