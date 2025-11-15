#using inbuilt module
import queue
n=int(input("enter no: of input:"))
L=queue.Queue(maxsize=n)

for _ in range (n):
    ele=input()
    L.put(ele)
print(L)
p=int(input("how many elements to pop :"))
for _ in range (p):
    print(L.get())

print(L)