def is_perfect_number(n, i=1, sum_divisors=0):
    # Базовый случай: если i достигло n, проверяем сумму делителей
    if i == n:
        return sum_divisors == n
    # Если i делитель n, добавляем его к сумме
    if n % i == 0:
        sum_divisors += i
    return is_perfect_number(n, i + 1, sum_divisors)
def main():
    user_input = int(input("Введите число: "))
    result = is_perfect_number(user_input)
    if result:
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()
