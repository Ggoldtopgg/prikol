import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Числа Фибоначчи")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("11. Завершить")

        choice = int(input("Введите номер операции: "))

        if choice == 11:
            break

        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        elif choice in [6, 7]:
            num = int(input("Введите число: "))
        else:
            num = float(input("Введите число: "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            result = num1 / num2
        elif choice == 5:
            result = num1 ** num2
        elif choice == 6:
            result = factorial(num)
        elif choice == 7:
            result = fibonacci(num)
        elif choice == 8:
            result = math.sin(num)
        elif choice == 9:
            result = math.cos(num)
        elif choice == 10:
            result = math.tan(num)
        else:
            print("Неверный выбор операции")
            continue

        print("Результат: ", result)

if __name__== "__main__":
    main()