import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    m = len(A)
    n = len(A[0])

    arr = np.zeros((n, m))

    for i in range(m):
        for j in range(n):
            arr[j][i] = A[i][j]

    return arr
