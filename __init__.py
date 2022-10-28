import numpy as np


array1 = np.array([1, 2, 3, 4, 5])
print(array1)
print("-----------------")

array2 = np.zeros((3, 2))
print(array2)
print(array2.shape)
print("-----------------")

array3 = np.ones((2, 4))
print(array3)
print("-----------------")

array4 = np.arange(3, 7)
print(array4)
print("-----------------")

array5 = np.linspace(0, 1, 5)
print(array5)
print("-----------------")

array6 = np.random.rand(2, 4)
print(array6)
print("-----------------")

array7 = np.zeros((4, 2), dtype=np.int32)
print(array7.dtype)

