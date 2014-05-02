def sum_lines_or_rows(matrix, sum_of_line):
    for line in matrix:
        current_sum = 0
        for row in line:
            current_sum += row
        if current_sum != sum_of_line:
            return False
    return True


def main_diagonal(matrix, sum_of_line):
    current_sum = 0
    for index in range(len(matrix[0])):
        current_sum += matrix[index][index]
    if current_sum != sum_of_line:
        return False
    return True


def back_diagonal(matrix, sum_of_line):
    current_sum = 0
    size = len(matrix[0]) - 1
    for i in range(size, -1, -1):
        current_sum += matrix[size-i][i]
    if current_sum != sum_of_line:
        return False
    return True


def magic_square(matrix):
    if len(matrix) < 1:
        return False
    sum_of_first_line = 0
    for i in matrix[0]:
        sum_of_first_line += i

    if not sum_lines_or_rows(matrix, sum_of_first_line):
        return False
    if not sum_lines_or_rows(list(zip(*matrix)), sum_of_first_line):
        return False
    if not main_diagonal(matrix, sum_of_first_line):
        return False
    if not back_diagonal(matrix, sum_of_first_line):
        return False
    return True
