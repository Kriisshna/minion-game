u,l= map(int,input().split())
for i in range(l+1,u):
    if i>=2:
        a=0
        for j in range (1,i+1):
            
            if i%j==0:
                a=a+1
        if a==2:
            print(i)       