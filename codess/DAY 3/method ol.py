from multipledispatch import dispatch
class methodoverloading:
    @dispatch(int,int)
    def add(self,a,b):
        x=a+b
        print(x)
        return x
    @dispatch(int,int,int)
    def add(self,a,b,c):
        x=a+b+c
        print(x)
        return x
obj=methodoverloading()
obj.add(4,5)

obj.add(4,3,9)

        