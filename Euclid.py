def gcd(a, b):
    # Базовый случай: если b равно 0, НОД равен a
    if b == 0:
        return a
    # Рекурсивный случай: продолжаем алгоритм Евклида
    else:
        return gcd(b, int(a) % int(b))
print("введите первое число")
user_input_1 = input()
print("введите второе число")
user_input_2 = input()
result = gcd(user_input_1,user_input_2)
print("НОД чисел равен",result)