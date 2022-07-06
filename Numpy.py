import numpy as np

one_dimensional_array = np.array([1.2, 2.4, 3.5])
print(one_dimensional_array)
# [1.2 2.4 3.5]

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)
##[[ 6  5]
## [11  7]
## [ 4  8]]

sequence_of_integers = np.arange(5, 9)
print(sequence_of_integers)
# [5 6 7 8]

reversed_sequence_of_integers = sequence_of_integers[::-1]
# [8 7 6 5]

random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)
# [74 56 64 64 77 59]

random_floats_between_0_and_1 = np.random.random([3])
print(random_floats_between_0_and_1)
# [0.19581127 0.69342686 0.54701759]

# Create a 3x3 matrix with values ranging from 0 to 8
Z = np.arange(9).reshape(3,3)
print(Z)

# Find indices of non-zero elements
nz = np.nonzero([1,2,0,0,4,0])
print(nz)


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
print(np.sqrt(x))


# Matrix / matrix product
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)


print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

print("transpose\n", x.T)

