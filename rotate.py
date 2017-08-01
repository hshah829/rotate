#!/bin/python

def rotate(matrix):
    size = len(matrix)
    layer_count = int(size / 2)

    for layer in range(0, layer_count):
        first = int(layer)
        last = int(size - layer - 1)
        i = int(first)
        while i < last:
            offset = int(i - first)

            # Save Top variable
            top = int(matrix[first][i])

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top
            i = i + 1

matrix = [[1, 2, 3], [4,5, 6], [7, 8, 9]]
print(matrix)
rotate(matrix)
print(matrix)