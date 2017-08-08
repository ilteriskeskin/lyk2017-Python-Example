import numpy as np

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])

v1 = np.arange(0, 5)

print(np.dot(A, A), "\n")

print(np.dot(A, v1), "\n")

M = np.matrix(A)
v = np.matrix(v1).T

print(A*A, "\n")

print(M*v, "\n")
