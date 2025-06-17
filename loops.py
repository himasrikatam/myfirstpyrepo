# conditional statements
a = input("Enter a: ")
if(int(a) %2==0):
  print("a is even")
else:
 print("a is odd")

b,c = input("enter values for b and c: ").split(" ")
print(b,c)
if(int(b)>int(c)):
    print("b is greater than c")
else:
    print("b is less than c")

# string
string ="HimasrireddyK"
print(string[::3])
print(string[::-1])
s= "hi"
r= "Ma"
print(s+" "+r)
print(len(string))
print(s[0],s[1])
print(s.upper())
print(r.lower())
p = " birbir PATAPIM"
print(p.strip())
print(p.replace('P','B'))
print(p.count('P'))
print(f"My name is {string}")
# escape sequence
print(f"{string}'s age is", int(input()))
print("Hello\\World\ttabbed\newline\rcarriage\bbackspace\fformfeed")
m = int(input())
p = int(input())
c = int(input())
total = m+p+c
per = (total/300)*100
if per>90:
    print("A grade")
elif per>80 and per<=90:
    print("B grade")
elif per>70 and per<=80:
    print("C grade")
else:
    print("Failed")
# palindrome
stringRev = string[::-1]
if(string == stringRev):
    print("palindrome")
else:
    print("not a palindrome")

# loops
l = int(input("Enter value for l: "))
while(l>0):
    print(l, end=" ")
    l -=1
for i in range(5,l):
    print(l, end=" ")
    l -=1
count=0
for i in range(len(string)):
    if string[i]=='H':
       count+=1
print("H count",count)
count=0
for i in string:
    if i == 'i':
        count+=1
print("i count", count)    

for i in range(1,6):
    for j in range(6,11):
        print(f"{i}*{j} = {i*j}")
# array multiplication
A = [int(x) for x in input("enter numbers: ").split()]
print("A= ", A)
B = [int(x) for x in input("enter numbers: ").split()]
print("B= ", B)
result = []
for i in range(l):
    if i == 5:
        continue
    elif i == 9:
        break
    print(i)