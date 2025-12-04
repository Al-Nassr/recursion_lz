def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        result = pascal_triangle(n - 1)
        current_row = [1]
        previous_row = result[-1]

        for i in range(len(previous_row) - 1):
            current_row.append(previous_row[i] + previous_row[i + 1])

        current_row.append(1)
        result.append(current_row)
        return result

def main():
    triangle = pascal_triangle(5)
    for row in triangle:
        print(row)
if __name__ == "__main__":
    main()
