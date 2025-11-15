# define 2 numerical data type variable as starting and design a calculator using class and object
# class-calc
# objects-values
# instance-
# method-operators


class calc():
    
    def add(self):
        print(a+b)
    def sub(self):
        print(a-b)
    def mult(self):
        print(a*b)
    def div(self):
        print(a/b)

obj=calc()
a=int(input())
operands=input()
b=int(input())

if operands=="+":
        obj.add()
elif operands=="-" :
        obj.sub()
elif operands=="*" :
        obj.mult()
elif operands=="/" :
        obj.div()

else:
      print("error")   
    