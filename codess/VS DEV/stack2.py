# def symbol(a):
b={"[":"]","{":"}","(":")"}
    # return(d[a])


def push(d):
    stack.append(d)

def pop():
    if stack:
        return(stack.pop())
    else:
        return None

stack=[]
n=int(input())
s=0
if n%2!=0:
    print("stack is invalid")
    s=s+1
else:
    for i in range (n):
        
        d=input()
        if d=="[" or d=="{" or d=="(":
            push(d)

        elif d=="]" or d=="}" or d==")":
            p= pop()
            
            if p is None or d != b[p]:
                print("stack is invalid")
                s=s+1
                break
        else:
            continue
        
if stack==[] and s==0:
    print("stack is valid")