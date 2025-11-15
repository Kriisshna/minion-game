class overloading:

    def add(self,a,b):
        print(a+b)
    def addstring(self,a,b):
        print(f"{a}"+f"{b}")

obj=overloading()
obj.add(3,2)
obj.addstring(3,2)