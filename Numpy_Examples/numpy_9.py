import numpy as np

m = np.random.rand(3,3)

print(m, "\n")
print(m.max(), "\n")
print(m.max(axis=0), "\n")
print(m.max(axis=1), "\n")

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])

n, m = A.shape

B = A.reshape((1, n*m))
print(B, "\n")

B[0,0:5] = 5

print(B, "\n")

print(A, "\n")

C = A.flatten()

print(C)

