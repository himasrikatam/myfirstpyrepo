print("hello world")
# variables
a=100
print("Print variable:", a)
# datatypes
b=[1,2,3,4,5]
print("datatype of b:", type(b))
c=1.5
print("datatype of c:", type(c))
d=a+c
print("datatype of d:", type(d))
br = 'birbirpatapim'
e = list(br)
f = [c]
print("datatype of e:", e, type(e))
print("datatype of f:", f,type(f))
is_true = bool(1)
is_false = bool(0)
print("datatype of is_true:",is_true, type(is_true))
print("datatype of is_false:",is_false, type(is_false))
# ascii values
char = 'H'
print("ascii value of char",ord(char))
print("ascii to char", chr(a))
div = a / c
print("div:",div)
print(a==c)
print(a>c)
print(a<c)
print(a!=c)
print("1 in b",1 in b)
print("18 in b",18 in b)
print(2>>3)
# input
name = input("Enter your name:")
age = int(input("Enter your age:"))
print("Hello ", name,"you're ", age," years old", end="!\n") # end="",changes the default behaviour which is \n
print(a,c, sep="-", end=" ended here\n")
t = input()
x,y,z = t.split(" ")
print("x,y,z:",x,y,z)