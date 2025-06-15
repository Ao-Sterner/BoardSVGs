import numpy as np

a = np.array([
    [1,2,3],
    [4,"hello",6]
])

print(a.dtype)

print(a[0][0])
print(a[0,0]) #possible error

print(type(a[0][0]))   #<class 'numpy.str_'>

print(a[0][0].dtype)

#you can type cast from int to str 
# but not the other way around
# unless the str is a number as below

b = np.array([
    [1,2,3],
    [4,"5",6]
]
, dtype=np.float32)  #this type casting is from C

print(b[0][0].dtype)
d = {'1':'A'}

c = np.array([
    [1,2,3],
    [4,d,6]
])
#3333333333333333333333333333333333333333
print(c.dtype)  # object
print(type(c[1][0]))

dd = np.array([
    [1,2,3],
    [4,44,6]],  dtype="<U7")

print(dd.dtype)  # object
print(type(dd[1][0]))