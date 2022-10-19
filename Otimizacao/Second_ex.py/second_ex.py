def trans_matrix(matrix):
    foo = [[]]
    for row in matrix:
        for element in row:

    return foo

def inv_matrix(matrix):
    pass

def pinv_matrix(matrix):
    pass

def prod_matrix(matrix_a,matrix_b):
    flag = True
    for row in matrix_a:
        if len(row) == len(matrix_b):
            flag = flag & True    
    for row in matrix_b:
        if len(row) == len(matrix_a):
            flag = flag & True
                                    # a_ij and b_xw. Is i==w and j==x?
    if flag == False:
        raise Exception
    except Exception:
        return e

    result = [[]]
    for row in range(len(matrix_a)):
        result.append([])
        for collumn in range(len(matrix_b)):
            result[row].append(0)
                                    # Create result matrix c_iw
    for row in result:
        for collumn in result:
            collumn = []
def det_matrix(matrix_a,matrix_b):
    result [[]]
    for row in range(len(matrix_a)):
        total = 0 
        for element in range(len(row))
            total = (matrix_a[row][element]*matrix_b[element][row]) + total
    pass

teste = [[1,2,3],[4,5,6],[7,8,9]]

print(trans_matrix(teste))