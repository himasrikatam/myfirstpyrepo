# dunder methods
class nameAge:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myName(self):
        print("Hello my name is ", self.name," and my age is ", self.age)
    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = nameAge('Himasri',21)
p1.myName()
print(p1)

# file handling
f = open("mydata.txt","r")
data = f.read()
line1 = f.readline()
line2 = f.readline()
print(data)
print("line1: ",line1)
print("line2: ",line2)
print(type(data))
f.close()
f = open("mydata.txt",'w')
overridesFile = f.write("this will override the entire mydata.txt")
# print("overridesFile: ", overridesFile)
f.close()
f= open("mydata.txt",'a')
appendtxt = f.write("\nThis line will append to the txt file")
f.close()
f = open("mydata.txt","r+")
Rplus = f.write("this will overide from the beginning of the mydata.txt. ")
f.close()
f = open("mydata.txt","w+")
f.read() # clears all the data to start writing from the beginning
Wplus = f.write("starting from the beginning after w+")
f.close()
# f = open("testingdata.txt",'x')
# x= f.write("testing  'x' ")
# f.close()
import os
# os.remove("testingdata.txt")
with open("mydata.txt",'r') as f:
    data2 = f.read()
    print(data2)
word="himasri"
with open("mydata.txt",'r') as f:
    data3= f.read()
    if(data3.find(word) !=-1):
        print("Found!!")
    else:
        print("Not Found.")
# exception handling
a = input("enter value for a: ")
print(f"Multiuplication table of {a} ")
try:
   for i in range(1,11):
      print(f"{int(a)} x {i} = {a*i}")
except Exception as e:
    print("invalid input!")
def testing():
    try:
        b = int(input("enter value for b: "))
        if(b>5 and b<15):
            raise ValueError("b should be less than 5 and greater than 15")
        A =[1,2,3,4,5,6,7,8,9]
        return print(A[b])
    except ValueError:
        return print("invalid value")
    except IndexError:
        return print("index out of range")
    finally:
        print("this is printing as this is kept in 'finally'")
x = testing()
print(x)
c = int(input("enter value for c: "))
if(c>5 and c<15):
    raise ValueError("c should be less than 5 and greater than 15")
# multithreading
import  threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(n):
    print(f"sleeping for {n} seconds")
    return time.sleep(n)

func(4)
func(10)
t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[10])
t1.start()
t2.start()
t1.join()
t2.join()
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func,4)
        future2 = executor.submit(func,5)
        future3 = executor.submit(func,6)
        future4 = executor.submit(func,10)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print(future4.result())
poolingDemo()