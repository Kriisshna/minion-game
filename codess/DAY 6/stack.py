
def push(d):
    stack.append(d)
def pop():
    stack.pop()

a=int(input())
p=int(input())
stack=[]
for i in range(a):
    d=int(input())
    push(d)
print(stack)
for i in range(p):  
    pop()
print(stack)
if stack==[]:
    print("stack is empty")
