# Quiz 1
# write a function that adds two vectors together
# def add(v, w):
#     res = []
#     for i in range(len(v)):
#         res.append(v[i] + w[i])
#     return res
#
#
# print(add([1, 2, 3], [4, 5, 6]))

# =====================================================
# def add(v, w):
#     """assert() is a built-in function that raises error if the condition is false"""
#     assert len(v) == len(w), "Vectors must be the same length"
#
#     """zip() is a built-in function that pairs together items from the passed"""
#     return [v_i + w_i for v_i, w_i in zip(v, w)]
#
#
# assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9], "Summation of 2 vectors is incorrect "
# =====================================================================================

# Quiz 2
# Write a function that multiplies a scalar and a vector
# def scalar_multiply(s, v):
#     res = []
#     for num in v:
#         res.append(s * num)
#     return res
#
#
# print(scalar_multiply(2, [2, 4, 6]))

# ==========================================================
# def scalar_multiply(s, v):
#     return [s * v_i for v_i in v]
#
#
# assert scalar_multiply(2, [2, 4, 6]) == [4, 8, 12]

# =============================================================
# Quiz 3
# Write a function that multiplies two vectors
# def dot(v, w):
#     assert len(v) == len(w), "Vectors must be the same length"
#     return sum(v_i * w_i for v_i, w_i in zip(v, w))
#
#
# assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32

# ===============================================================================
# Quiz 4
# Write a function that takes a matrix and gives you its shape.
# def shape(A):
#     num_rows = len(A)
#     num_cols = len(A[0]) if A else 0
#     return num_rows, num_cols
#
#
# assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)
# ==================================================================================
# Quiz 5
# Write a function that adds two matrices
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[1, 2, 3], [4, 5, 6]]
#
#
# def add(a, b):
#     return [a_i + b_i for a_i, b_i in zip(a, b)]
#
#
# def matrix_add(A, B):
#     return [add(A_i, B_i) for A_i, B_i in zip(A, B)]
#
#
# print(matrix_add(A, B))
# ================================================================
# Quiz 6
# Write a function that multiply two matrices element-wise
# A = [[1, 2, 3], [4, 5, 6]]
# B = [[1, 2, 3], [4, 5, 6]]
#
#
# def mult_element_wise(v, u):
#     assert len(v) == len(u), "Vectors must be the same length"
#     return [v_i * u_i for v_i, u_i in zip(v, u)]
#
#
# def matrix_mult_element_wise(A, B):
#     c = []
#     for i in range(len(A)):
#         c.append(mult_element_wise(A[i], B[i]))
#     return c
#
#
# print(matrix_mult_element_wise(A, B))
# ================================================================
# Quiz 7
# Write a function that multiply a vector with a matrix
"""def dot(v, u):
     assert len(v) == len(u), "Vectors must be the same length"
     return sum([v_i * u_i for v_i, u_i in zip(v, u)])


def matrix_mult_vector(A, b):
     c = []
     for i in range(len(A)):
         c.append(dot(A[i], b))
     return c


A=[[1,2,3],
   [4,5,6]]
B=[[1,0,3],
   [6,5,6],
   [1,2,3]]
print(matrix_mult_vector(A,B))"""
# =======================================================
# Quiz 8
# Write a function that multiplies a matrix by a scalar
def scaler_multiply(c, v):
     return [c * v_i for v_i in v]


def matrix_mult_scaler(A, b):
     c = []
     for i in range(len(A)):
         c.append(scaler_multiply(b, A[i]))
     return c


A = [[1, 2], [3, 4], [5, 6]]
b = 0.5
print(matrix_mult_scaler(A, b))
