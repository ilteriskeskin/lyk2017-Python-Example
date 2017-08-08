import numpy as np

d1 = np.diag([1,2,3])
d2 = np.diag([1,2,3], k=2)

m1 = np.zeros((5,4))
m2 = np.ones((2,3))

print(d1, "\n")
print(d2, "\n")
print(m1, "\n")
print(m2, "\n")

