import numpy as np

A = np.array([[n+m*10 for n in range(5)] for m in range(5)])
M = np.matrix(A)
print(M, "\n")

if (M > 20).any():
    print("at least one element in M is larger than 20 \n")
else:
    print("None \n")

if (M > 5).all():
    print("all elements in M are larger than 5 \n")
else:
    print("all elements in M are not larger than 5 \n")