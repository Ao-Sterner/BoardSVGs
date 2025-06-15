import numpy as np

a = [1,2,3,4,5]

b = np.array(a)
print(b)

mul = np.array([[[1,2,3] ,
                 [4,5,6],
                 [7,8,9]]
                 ,
                 [[1,2,3] ,
                 [4,5,6],
                 [7,8,9]],
                 
                 [[1,2,3] ,
                 [4,5,6],
                 [7,8,9]]])



print(mul[0])
print(mul[0,1,2])
print(mul.shape)
print(mul.ndim)
print(mul.size)
print(mul.dtype) #numpy is written in C