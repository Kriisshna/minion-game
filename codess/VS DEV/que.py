que=[]
n=int(input("enter no: of input:"))
for _ in range (n):
    ele=input()
    que.append(ele)

print(que)
p=int(input("how many elements to pop :"))
for _ in range (p):
    que.pop(0)
print(que)