import numpy as np
a = np.full((2,3,4), 8)
print(a)

b = np.full((3,5,4), 8)
print(b)

c = np.zeros((2,3,2)) #can replace zeros with ones
print(c)

a = np.empty((5,5,5)) #values aren't initialized
#in c you allocate memory and all this does is 
# reserve space

x = np.arange(0,100,5) #start, end, step val
print(x)

z = np.linspace(0,1000, 4) #start, end, number 
#of values (evenly distributed)

4