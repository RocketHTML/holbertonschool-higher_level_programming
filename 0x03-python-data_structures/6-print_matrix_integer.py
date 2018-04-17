#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j + 1 == len(matrix[i]):
                last = '\n'
            else:
                last = ' '
            print('{:d}'.format(matrix[i][j]), end=last)

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
