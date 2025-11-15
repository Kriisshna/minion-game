# a=int(input("enter the first number"))
# b=int(input("enter the second number"))


# #arithmatic
# print(a,"+",b,"=",a+b)
# print(a,"/",b,"=",a/b)
# print(a,"-",b,"=",a-b)
# print(a,"*",b,"=",a*b)
# print(a,"//",b,"=",a//b)
# print(a,"%",b,"=",a%b)
# print(a,"**",b,"=",a**b)

# a+=b
# print(a)


# print(a<b)
# print(a>=b)
# print(a>b)
# print(a<=b)
# print(a==b)

# logical operators

# print((a<b)and(a>b))
# print((a<b)or(a>b))
# print(not a==b)

# # bitwise
# print(a,"&",b,"=",a&b)
# print(a,"|",b,"=",a|b)
# print(a,"^",b,"=",a^b)
# print(a,"<<",b,"=",a<<b)
# print(a,">>",b,"=",a>>b)

# print(a is b)
# print(a is not b)

a=[2,3,4]
# b=a
b=a.copy()
b[0]=7
print(a is b)
print(7 in a)
print(7 in b)