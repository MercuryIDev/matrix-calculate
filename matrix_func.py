#Функция суммирования матрицы
def matrix_sum(matrix_one, matrix_two):
    matrix_sum = []
    for i in range(len(matrix_one)):
        row = []
        for j in range(len(matrix_one[0])):
            row.append(matrix_one[i][j] + matrix_two[i][j])
        matrix_sum.append(row)
    return matrix_sum
