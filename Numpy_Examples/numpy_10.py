import numpy as np

a = np.array([[1,2], [3,4]])

print((np.repeat(a, 3)), "\n")

print(np.tile(a,3), "\n")

b = np.array([[5,6]])
print(np.concatenate((a, b), axis=0), "\n")
print(np.vstack((a,b)), "\n") #vertical stack
print(np.hstack((a,b.T)), "\n") #horizontal stack