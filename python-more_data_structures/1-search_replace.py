#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        new_i = []
        for idx in i:
            new_i.append(idx * idx)
        new_matrix.append(new_i)
    return new_matrix
