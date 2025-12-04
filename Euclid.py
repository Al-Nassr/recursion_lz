def gcd(a, b):
    # Базовый случай: если b равно 0, НОД равен a
    if b == 0:
        return a
    # Рекурсивный случай: алгоритм Евклида
    return gcd(b, a % b)
def main():
    print("Введите первое число:")
    user_input_1 = int(input())

    print("Введите второе число:")
    user_input_2 = int(input())
    result = gcd(user_input_1, user_input_2)
    print("НОД чисел равен", result)
if __name__ == "__main__":
    main()
