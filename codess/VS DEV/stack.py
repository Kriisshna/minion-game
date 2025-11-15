stack=[]
n=int(input())
for _ in range (n):
    stack.append(int(input()))
print(stack)

p=int(input("no: of elements to be popped:"))
for _ in range (p):
    print(stack.pop())
print(stack)
if stack==[]:
    print("stack is empty")
    