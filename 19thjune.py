# functional programming concepts
def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res
l1=[1,2,3,4,5]
newl = list(map(fact,l1)) # map(func_name,parameters)
print(newl)
def filterfunc(n):
    return n>3
newl1 = list(filter(filterfunc,l1)) # filter(func_name,parameters)
print("newl1: ", newl1)
newl2 = list(map(lambda x:x*x, l1)) # lambda
print("newl2: ", newl2)
from functools import reduce
sum = reduce(lambda x,y:x*y,l1) # lambda
print("sum", sum)
# linear algebra

# linear transformations => functions to move around space(linearly=> grid lines are //le to each others)
# ex: matrix multiplication of i and j vectors to span(x and y) abt which it has to move around space
# sq matrix mult represnts composition and shear at a time ex. 90 deg rotation and shear(move around space)i.e 2 transformations
# det is by how much does the area change after the transformation
# inverse matrix is used when a set of eqs need to be solved Ax'=v'=> A'(Ax')=A'v'=> x' = A'v'

# numpy
import numpy as np
np1= np.array([1,2,3,4,5,6,7,8,9])
print("np1: ", np1)
print("np1 length: ", np1.shape)
print("range: ", np.arange(9))
print("range with step: ",np.arange(0,10,2))
print("array with 0s: ", np.zeros(10))
print("Multi dim array with 0s: ", np.zeros((4,5))) # (dim,size)
print("array with 9s: ", np.full((4),9)) # (no.of,ele)
print("multidim array with 9s: ", np.full((4,10),9)) # (dim,size),ele
np2= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(np2[1][4]) #4th item in 1st row
print(np2[0][2]) #2nd item in 0th row
print(np2[0:2,1:3]) # 0:2 is 0,1 rows
# np.sqrt(), np.absoulte(), np.exp(), np.max(), np.min(), np.sign(), 
# np.sin(), np.log(), 
np2 = np.random.randint(10,51,size=16)
print("random: ", np2)
print("identity maxtrix: ", np.eye(5))
print("reverse: ", np1[::-1])
np3= np.arange(16)
print("np3: ", np3)
print("1d to 4d", np2.reshape(4,4))
# Implementing matrix operations using NumPy
np4 = np.random.randint(1,100,size=(2,2))
np5 = np.random.randint(1,100,size=(2,2))
print("np4: ", np4)
print("flatten: ", np4.flatten())
print("np5: ", np5)
print("np4 x np5: ",np.dot(np4,np5))
print("np4 transpose: ",np.transpose(np4))
print("np4 inverse: ",np.linalg.inv(np4))
print("det of np4: ", np.linalg.det(np4) )