
def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if type(matrix[0]) is list:
        starting_lenght = len(matrix[0])

    for L in matrix:
        if type(L) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(L) != starting_lenght:
            raise TypeError("Each row of the matrix must have the same size")
        for n in L:
            if type(n) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    new_list = []
    new_matrix = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for L in matrix:
        for n in L:
            new_list.append(round((n / div), 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
