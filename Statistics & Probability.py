# Statistics
import numpy as np


# mean(vector, matrix)

# mean for vectors
# v = np.array([1, 2, 3, 4, 5, 6])
# m = np.mean(v)
# print(f"Vector : {v}\nMean : {m}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++
# mean for matrices
# M = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])
#
# col_mean = np.mean(M, axis=0)
# row_mean = np.mean(M, axis=1)
#
# print(f"Matrix :\n{M}\nmean of columns : {col_mean}\nmean of rows : {row_mean}")
# ==================================================================================

# variance(vector, matrix)

# variance for vectors
# v = np.array([1, 2, 3, 4, 5, 6])
# vari = np.var(v)
# print(f"Vector : {v}\nVariance : {vari}")
# +++++++++++++++++++++++++++++++++++++++++++++++++++
# variance for matrices
# M = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])
#
# col_variance = np.var(M, axis=0)
# row_variance = np.var(M, axis=1)
#
# print(f"Matrix :\n{M}\nvariance of columns : {col_variance}\nvariance of rows : {row_variance}")
# =================================================================================================
# Standard Deviation

# M = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])
# col_std = np.std(M, axis=0)
# row_std = np.std(M, axis=1)
# print(f"Matrix :\n{M}\nstd of columns : {col_std}\nstd of rows : {row_std}")
# =================================================================================
# Quiz 1
# Write a function stats() that takes any sequence of numbers and give back its mean, variance and std.

def stats(variable, axis=0):
    mat = np.array(variable)

    if len(mat.shape) == 1:
        mean = np.mean(mat)
        var = np.var(mat)
        std = np.std(mat)
    else:
        mean = np.mean(mat, axis=axis)
        var = np.var(mat, axis=axis)
        std = np.std(mat, axis=axis)

    return mean, var, std


V = np.array([1, 2, 3, 4, 5])

M = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print(f"For V : {V}\nmean : {stats(V)[0]}\nvariance : {stats(V)[1]}\nstd : {stats(V)[2]}\n")

print(f"For M :\n{M}\nmean of cols : {stats(M, axis=0)[0]}\nvariance of cols : {stats(M, axis=0)[1]}\nstd of cols : {stats(M, axis=0)[2]}\n")

print(f"For M :\n{M}\nmean of rows : {stats(M, axis=1)[0]}\nvariance of rows : {stats(M, axis=1)[1]}\nstd of rows : {stats(M, axis=1)[2]}")

# ====================================================================================

# Calculate Covariance

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 4, 3, 2, 1])
#
# sigma_matrix = np.cov(x, y)
#
# sigma = sigma_matrix[0, 1]
#
# print(f"X = {x}\nY = {y}\nCov(X, Y) =\n{sigma_matrix}\nsigma = {sigma}")

# =====================================================================================================

# Calculate Correlation

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([5, 4, 3, 2, 1])
#
# sigma_matrix = np.corrcoef(x, y)
#
# sigma = sigma_matrix[0, 1]
#
# print(f"X = {x}\nY = {y}\nCov(X, Y) =\n{sigma_matrix}\nsigma = {sigma}")

