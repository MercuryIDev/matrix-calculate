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

# Создание пустой матрицы и заполнение данных
def create_and_fill_matrix():
    # Создаем пустую матрицу
    rows, cols = check_valid()
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0)
        matrix.append(row)
    
    # Заполняем матрицу
    print("\nStarting matrix fill...")
    
    for i in range(rows):
        for j in range(cols):
            print(f"\nCurrent position: [{i}][{j}]")
            temp_matrix = [row[:] for row in matrix]
            temp_matrix[i][j] = "-"
            
            print_matrix(temp_matrix, "Fill this position")
            
            while True:
                try:
                    value = int(input("Enter value: "))
                    matrix[i][j] = value
                    break
                except ValueError:
                    print("Please enter a valid integer!")
            print_matrix(matrix)
    
    return matrix

# Функция суммирования матрицы
def matrix_sum(matrix_one, matrix_two):
    try:
        if len(matrix_one) != len(matrix_two) or len(matrix_one[0]) != len(matrix_two[0]):
            raise ValueError("Matrices must have same dimensions")
        
        matrix_sum = []
        for i in range(len(matrix_one)):
            row = []
            for j in range(len(matrix_one[0])):
                row.append(matrix_one[i][j] + matrix_two[i][j])
            matrix_sum.append(row)
        return matrix_sum
        
    except (ValueError, TypeError, IndexError) as e:
        print(f"ERROR! Cannot sum matrices: {e}")
        return None


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