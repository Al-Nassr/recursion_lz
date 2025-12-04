
def partition(n, min_number=1):
    if n == 0:
        return [[]]  # Базовый случай: если осталось 0, возвращаем пустое разбиение
    parts = []
    for i in range(min_number, n + 1):  # Проходим от min_number до n
        for part in partition(n - i, i):  # Рекурсивный вызов для остатка
            parts.append([i] + part)  # Добавляем текущее число к каждому разбиению
    return parts
def print_partitions(n):
    partitions = partition(n)
    for p in partitions:
        print(p)
def main():
    n = int(input("Введите число, которое хотите разложить на сумму целых чисел: "))
    print_partitions(n)
if __name__ == "__main__":
    main()

