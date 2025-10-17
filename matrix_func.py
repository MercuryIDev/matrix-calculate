def check_valid():
    while True:
        try:
            i_input = int(input('Enter (i) string: '))
            j_input = int(input('Enter (j) column: '))

            if i_input <=0:
                 print(f'Value i: {i_input} <= 0 !')
                 continue
            if j_input <=0:
                 print(f'Value i: {j_input} <= 0 !')
                 continue
            
            return i_input, j_input

        except ValueError:
            print('integer is required!')    

# Функция ручного ввода матрицы
def create_null_matrix():
    rows, cols = check_valid()

    matrix_list = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix_list.append(row)

    print_matrix(matrix_list)
    return matrix_list
    
# Функция ручного заполнения матрицы
def input_fill_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    print("Starting matrix fill...")
    
    for i in range(rows):
        for j in range(cols):
            # Показываем матрицу с указателем на текущую позицию
            print(f"\nCurrent position: [{i}][{j}]")
            temp_matrix = [row[:] for row in matrix]  # Копируем матрицу
            temp_matrix[i][j] = "-"  # Помечаем текущую позицию
            
            print_matrix(temp_matrix, "Fill this position")
            
            # Получаем значение от пользователя
            while True:
                try:
                    value = int(input("Enter value: "))
                    matrix[i][j] = value
                    break
                except ValueError:
                    print("Please enter a valid integer!")
    
    return matrix

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
        print("[", end="")
        for j, element in enumerate(row):
            if j < len(row) - 1:
                print(f"{element}", end=", ")
            else:
                print(f"{element}", end="")
        print("]")
    print()



# Тестовые данные
matrix_one = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

matrix_two = [[1, 2, 3],
              [0, 5, 6],
              [0, 0, 9]]

# # Вычисление и вывод
# result = matrix_sum(matrix_one, matrix_two)

# print_matrix(matrix_one, "Matrix One")
# print_matrix(matrix_two, "Matrix Two")
# print_matrix(result, "Sum Result")
test_matrix = create_null_matrix()
add_value = input_fill_matrix(test_matrix)

print_matrix(add_value)


