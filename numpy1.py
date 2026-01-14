import numpy as np
# import array
# print(np.__version__)

a = np.array([1, 2, 3])
b = np.array([[1, -2], [3.9, 4]])



# print(a + 2)      # [3 4 5]
# print(a * 2)      # [2 4 6]

# print(b *2)

# print(b[0][0])

# print(b)

# arr = np.linspace(1,100,100)
# print(arr)

# arr = np.full((3,4),"#")

# arr = np.full((2),9)
# arr = np.full((2,5),9)

# arr = np.ones(12)
# arr = np.ones((12,2))

# arr = np.arange(1,20,2)  ### Odd number 0 to 19
# arr = np.arange(0,21,2) ### Even number 0 to 20



# arr = np.eye(5)

# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]


# print(arr)


A = np.array([
    [1,2,3,4],
    [2,3,4,5],
    [2,3,4,5],
    [2,3,4,5],
])


A = np.matrix('1,2,3;4,5,6;7,8,1')
B = np.matrix('1,2,3;4,5,6;7,8,9')
# B = np.matrix('1,2,3;5,6,7;8,9,1')

# print(np.diagonal(A))

# print(A.max())

# print(A)
# print(B)
print(A*B)

print(A+B)

print(A-B)