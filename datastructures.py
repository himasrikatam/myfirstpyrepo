from collections import deque
# stacks LIFO
stack=[]
n = int(input("Enter n: "))
for i in range(n):
    stack.append(input("enter stack item: "))
print("LIFO")
while stack:
    print("popped: ", stack.pop())
# queue FIFO to pop we should use .pop(0) which takes time as it is list(in list the end operations are faster) sop we use deque
queue=[]
n = int(input("Enter n: "))
for i in range(n):
    queue.append(input("enter queue item: "))
print("queue: ", queue)
queue = deque(queue)
print("dequeue: ", queue)
print("FIFO")
while queue:
    print("popped: ", queue.pop()) #can you popleft() to pop from left
# hash map
hashmap ={}
n = int(input("Enter n: "))
for i in range(n):
    key = input("enter key: ")
    value = input("enter value: ")
    hashmap[key] = value
print("Hashmap elements: ")
for k,v in hashmap.items():
    print(k ,"=>", v)
# linked lists