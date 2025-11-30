import numpy as np

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])

print("A + B =", A + B)
print("A - B =", A - B)
print("A * B =", A * B)
print("A / B =", A / B)

C = np.concatenate((A, B))
print("Конкатенація A і B =", C)

print("Максимум =", C.max())
print("Мінімум =", C.min())
print("Сума =", C.sum())
print("Добуток =", C.prod())
