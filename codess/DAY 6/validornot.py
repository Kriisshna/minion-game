
def push(d):
    stack.append(d)
def pop():
    if stack:
        return stack.pop()
    else:
        return None
dict={"(":")","[":"]","{":"}"}
n=int(input())
stack=[]
if n%2==0:
    for i in range(n):
        d=input()
        if d=="(" or d=="[" or d=="{" :
            push(d)
        elif d==")" or d=="]" or d=="}":
            p=pop()

            if p is None or d!=dict[p]:
                print("invalid")
                break
            
            
        else:
            print("error")
            break
else:
    print("error")
if stack==[]:
    print("valid")

