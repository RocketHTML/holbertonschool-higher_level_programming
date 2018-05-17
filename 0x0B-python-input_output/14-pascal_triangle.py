#!/usr/bin/python3


def pascal_triangle(n):
    def create(n):
        m = []
        for i in range(n):
            m.append([0 for j in range(i+1)])
        return m

    def compute(m, i, j):
        if j == 0 or j == len(m[i]) - 1:
            return 1
        left = m[i - 1][j - 1]
        right = m[i - 1][j]
        return left + right

    triangle = create(n)
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] = compute(triangle, i, j)
    return triangle
