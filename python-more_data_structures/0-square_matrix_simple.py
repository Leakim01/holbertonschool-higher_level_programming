#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [] 
    new_list = []
    for each_list in matrix:
        new_list = []
        for each_elem in each_list:
            square = each_elem ** 2
            new_list.append(square)
        new_matrix.append(new_list)
    return new_matrix
