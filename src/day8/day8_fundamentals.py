import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)

# Vectorized vs Loop example
arr = np.random.rand(1000000)
print("Random number:\n", arr)

# Vectorized
squared = arr ** 2
print("Squared (vectorized):\n", squared)

#zero dimensional array
zeroarray = np.zeros((4,2))   
print("zeroarray:\n", zeroarray)  # Output: 42

#one dimensional array
onedarray = np.array([1, 2, 3, 4, 5])  
print("onedarray:\n", onedarray)  # Output: [1 2 3 4 5]

#two dimensional array
twodarray = np.array([[1, 2, 3], [4, 5, 6]])
print("twodarray:\n", twodarray)

#three dimensional array
threedarray = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("threedarray:\n", threedarray)   

#reshaping arrays
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print("Reshaped array:\n", reshaped)

#vertical stacking
a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print("Vertically stacked array:\n", vstacked)

#horizontal stacking
hstacked = np.hstack((a, b))
print("Horizontally stacked array:\n", hstacked)
print("\n")

#statistical functions
data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print("Mean:",np.mean(data))
print("Median:",np.median(data, axis=0))
print("Standard Deviation:",np.std(data))
print("Variance:",np.var(data))
print("\n")

#matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.multiply(A, B)
print("Matrix A:\n", A)
print("Matrix B:\n", B) 
print("Matrix C (A * B):\n", C)

