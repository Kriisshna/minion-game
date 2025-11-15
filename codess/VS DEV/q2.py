m=[]
n=int(input())
for i in range (n):
        m.append(list((map(int,input("enter the row").split()))))
print(" ")


print("diagonal elements")
for i in range (n):
    for j in range (n):
        if i==j:
            print(m[i][j])
        else:
            print(end="")    



# print("non-diagonal elements")
# for i in range (n):
#     for j in range (n):
#         if i!=j:
#             print (m[i][j])   
# print(" ")            



# print("upper diagonal elements")
# for i in range (n):
#     for j in range (n):
#         if i<j:
#             print (m[i][j])
# print(" ")            



# print("lower diagonal elements")
# for i in range (n):
#     for j in range (n):
#         if i>j:
#             print (m[i][j])
# print(" ")            
