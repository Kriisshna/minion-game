def check(a,s,e,n):
    if(s+1==e-1):
        for k in range(1,n+1):
            if(a[s]%k==0):
                a[s+1]=k
                global count
                count = count+1
                print(a)
    else:
        for k in range(1,n+1):
            if(a[s]%k==0):
                a[s+1]=k
                check(a,s+1,e,n)

n=int(input())
k=int(input())
a=[0]*k
count = 0
if(k==1):
    count=n
else:
    for i in range(1,n+1):
        a[0]=i
        check(a,0,k,n)
print(count)