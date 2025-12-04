def pascal_triangle(n):
    if n == 1:
        return [[1]] 
    else:
        result = pascal_triangle(n-1)  # Рекурсивный вызов: получаем треугольник из (n-1) строк
        current_row = [1]  # Начинаем формировать новую строку
        previous_row = result[-1] # Берём последнюю строку уже построенного треугольника
        for i in range(len(previous_row)-1):  # Строим середину строки: каждый элемент — сумма двух соседних сверху
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1] # Завершаем строку единицей
        result.append(current_row)
        return result
triangle = pascal_triangle(5)
for row in triangle:
    print(row)