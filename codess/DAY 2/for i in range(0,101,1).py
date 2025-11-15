print("odd numbers are:\n")   
for i in range(0,101,1): 
    if i&1==1:
        print(i,end=' ')

print("\neven numbers are:\n")   
for i in range(0,101,1): 
    if i&1==0:
        print(i,end=' ')