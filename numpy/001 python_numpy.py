import numpy as np

#create one dimensional array
first = np.array([4,5,6], dtype='int16')
print(first)
print(type(first))


#create two dimensional array
second = np.array([[4,5,6],[7,8,9]])
print(second)

#get some array information
print("Dimension of array - first: ")
print(first.ndim)
print("Dimension of array - second: ")
print(second.ndim)
print("Shape of array first: ")
print(first.shape)
print("Shape of array second")
print(second.shape)
print("Datatype of array - first: ")
print(first.dtype)

third = np.array([[4.0,5.0,6.0],[7,8,9]])
print(third)

print("Datatype of array - second: ")
print(second.dtype)

print("Datatype of array - third: ")
print(third.dtype)


print("Array size - first:")
print(first.itemsize)
print("Count of values - first: ")
print(first.size)

print("Array size - second:")
print(second.itemsize)
print("Count of values - second: ")
print(second.size)

print("Array size - third:")
print(third.itemsize)
print("Count of values - third: ")
print(third.size)


print("Storage in bytes - first: ")
print(first.nbytes)

print("Storage in bytes - second: ")
print(second.nbytes)

print("Storage in bytes - third: ")
print(third.nbytes)


#access and update numpy arrays! -> element, rows, column

fourth = np.array([[8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8]])
print(fourth.shape)
print(fourth)

#arrayname[row, column]
print(fourth[1, 2])
print(fourth[1, 0])

#reverse order
print(fourth[0, -3])
#normal order
print(fourth[0, 1 ])

#rows only
print(fourth[1])
print(fourth[0])

#column only
print(fourth[:,2])
print(fourth[:,0])

#extract from middle of array
# arrayname[startindex:endindex:step]
print("For row 0 get column 0 to length 6")
print(fourth[0,0:6])

print("For row 0 get column 0 to length 8 with step 2")
print(fourth[0,0:8:2])


print("For row 1 get column 2 to length 8 with step 2")
print(fourth[1,2:8:2])


print("For row 1 get column 2 to length 6 with step 2")
print(fourth[1,2:6:2])

#update value in 2D array
"""
[[8 7 6 5 4 3 2 1]
 [1 2 3 4 5 6 7 8]]
 """
fourth[1, 4 ] = 44
print(fourth)

#update specific column to single value
"""
[[ 8  7  6  5  4  3  2  1]
 [ 1  2  3  4 44  6  7  8]]
"""
fourth[:,6] = 88
print(fourth)
"""
[[ 8  7  6  5  4  3 88  1]
 [ 1  2  3  4 44  6 88  8]]
"""
fourth[:,5] = [10, 100]
print(fourth)
"""
[[  8   7   6   5   4  10  88   1]
 [  1   2   3   4  44 100  88   8]]
"""