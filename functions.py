a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
def sum(a,b):
    return a+b 
print("Sum of a and b= ", sum(a,b))
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i 
    return res 
print("Factorial: ", factorial(a))
def countVowels(s):
    vowels = "aeiouAEIOU"
    count = 0 
    for ch in s:
        if ch in vowels:
            count +=1
    return count
print("Vowels count: ", countVowels("Himasri"))
A = [int(x) for x in input("enter numbers: ").split()]
print("A= ", A)
def largestNumber(arr):
    largest = arr[0]
    for i in arr:
        if i>largest:
            largest = i
    return largest 
print("Largest Number in A= ", largestNumber(A))
# lists
List = [29, 26, 25 , 24, 99, 79] 
# print(List.insert(2,18)) 
print(List.append(36))
print(List.pop(1))
print(List.pop())
print(List.insert(2,18))
print(List.extend([130,31,32,33]))
print(min(List))
print(max(List))
# tuples
tup = (23, 24, 25, 26 , 27)
print(tup.index(24))
# sets
Set = [ 77, 78,98, 99, 100]