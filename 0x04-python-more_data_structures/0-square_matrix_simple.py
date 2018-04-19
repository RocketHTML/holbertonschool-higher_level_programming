#!/usr/bin/python3
def copy(mx, rx, i):
    if len(rx) == len(mx):
        return
    rx.append(mx[i][:])
    copy(mx, rx, i + 1)


def matrix_xy(mx, x, y):
    mx[x][y] *= mx[x][y]
    if y == len(mx[x]) - 1:
        x += 1
        y = 0
        if x == len(mx):
            return mx
    else:
        y += 1
    return matrix_xy(mx, x, y)


def square_matrix_simple(matrix=[]):
    clone = []
    copy(matrix, clone, 0)
    if len(clone) > 0:
        return matrix_xy(clone, 0, 0)
    else:
        return matrix

if __name__ == '__main__':
    matrix = []

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)
