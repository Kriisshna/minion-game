class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlell:
    def __init__(self):                                         
        self.head=None
    def userip(self,n,fd):   
        fn=node(fd)
        obj.head=fn
        for _ in range (1,n):
            new=int(input())
            nn=node(new)
            fn.next=nn
            fn=nn
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,end='')
                if temp.next!=None:
                    print("->",end='')
                else:
                    print("")
                temp=temp.next
            # temp.next
obj=singlell()
n=int(input())
fd=int(input())
obj.userip(n,fd)
obj.display()