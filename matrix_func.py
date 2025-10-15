def check_valid():
    while True:
        try:
            i_input = int(input('Enter (i) string: '))
            j_input = int(input('Enter (j) column: '))

            if i_input <=0:
                 print(f'Value i: {i_input} <= 0 !')
            if j_input <=0:
                 print(f'Value i: {j_input} <= 0 !')
            else:
                break

        except ValueError:
            print('integer is required!')

#def create_null_matrix(val_i, val_j):
    


# Функция суммирования матрицы
def matrix_sum(matrix_one, matrix_two):
    matrix_sum = []
    for i in range(len(matrix_one)):
        row = []
        for j in range(len(matrix_one[0])):
            row.append(matrix_one[i][j] + matrix_two[i][j])
        matrix_sum.append(row)
    return matrix_sum

# Пока использую вписанные матрицы для проверки функций

# Функция для красивого вывода матрицы
def print_matrix(matrix, name="Matrix"):
    print(f"{name}:")
    for row in matrix:
        print(" [", end="")
        for j, element in enumerate(row):
            if j < len(row) - 1:
                print(f"{element:3}", end=", ")
            else:
                print(f"{element:3}", end="")
        print(" ]")
    print()

# Тестовые данные
matrix_one = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

matrix_two = [[1, 2, 3],
              [0, 5, 6],
              [0, 0, 9]]

# Вычисление и вывод
result = matrix_sum(matrix_one, matrix_two)

print_matrix(matrix_one, "Matrix One")
print_matrix(matrix_two, "Matrix Two")
print_matrix(result, "Sum Result")
