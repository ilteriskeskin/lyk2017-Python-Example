import numpy as np

# M = np.random.rand(3,3)
#
# print(M, "\n")
# print(M[1], "\n")
# print(M[1,1], "\n")
# print(M[1,:], "\n")
# print(M[:,1], "\n")
#
# A = np.array([1,2,3,4,5])
#
# print(A[1:3], "\n")
# print(A[::2], "\n")
# print(A[-1], "\n")

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
print(A, "\n")

row_indices = [1,2,3]
print(A[row_indices], "\n")

col_indices = [1,2,-1]
print(A[row_indices, col_indices], "\n")

which = [1,0,1,0,2]
choices = [[-2,-2,-2,3,8], [5,5,4,5,8], [9,9,9,9,9]]
print(np.choose(which,choices), "\n")
