#0,60,100,40,20,80,90,200,30,15,61,120,84,16,55,190,85,21
from array import *
a=[]
n=int(input())

for i in range(n):
    x=int(input())
    a.append(x)

print(a)
s=[]
if a[0]>a[1]:
        s.append(a[0]) 
for i in range(n-1):
    if a[i-1]<a[i]>a[i+1]:
        s.append(a[i])
    
if a[n-1]>a[n-2]:
    s.append(a[n-1])     
print("peak values:",s)

#peak value
large=0
for i in range(len(s)):
     if s[i]>large:
        large=s[i]
print("largest:",large)

    
# print("max",max(s))
#reverse 
r=[0]*n
for i in range(n):
    r[i]=a[n-1-i]
print(r)
# print(a[::-1])