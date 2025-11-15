# implementattion using inbuilt
import queue
n=int(input())
L=queue.Queue(maxsize=n)
for i in range (n):
    d=int(input())
    L.put(d)

print(L.get())