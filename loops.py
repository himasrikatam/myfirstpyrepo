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