#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for h in matrix:
        for v in h:
            if v == h[-1]:
                print("{:d}".format(v), end = "$\n")
            else:
                print("{:d}".format(v), end=" ")
    print("$")
