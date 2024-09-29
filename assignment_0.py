import numpy as np


print("\n--- Linear Algebra ---")

A = np.array([[1, 1, -1, -1],
             [2, 5, -7, -5],
             [2, -1, 1, 3],
             [5, 2, -4, -2]])

b = np.array([[1, -2, 4, 6]])
b = np.transpose(b)

A_inv = np.invert(A)
x = np.dot(A_inv, b)

print("\nExercise b\n")
print("The inverse of matrix A is: ", A_inv)
print("The solution of x is: ", x)


# Positive Semidefinitive matrices
# xT.A.x is a scalar

dot_1 = np.dot(A, x)
dot_2 = np.dot(np.transpose(x), dot_1)
print("\nExercise a\n")
print(dot_1)
print("Quadratic Form: ", dot_2)
