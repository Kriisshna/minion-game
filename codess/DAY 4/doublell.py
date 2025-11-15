class node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class doublell:
    def __init__(self):
        self.head=None
    def insbeg(self,data):
        nb=node(data)
        t=self.head
        nb.next=t
        t.prev=nb
        self.head=nb
    def inslast(self,data):
        n=node(data)
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next=n
        n.prev=temp
    def inbtw(self,data,p):
        n=node(data)
        temp=self.head
        for _ in range(p-1):
            temp=temp.next
        n.next=temp.next
        n.prev=temp
    def userip(self,n,fd):   
        fn=node(fd)
        obj.head=fn
        for _ in range (1,n):
            new=int(input())
            nn=node(new)
            fn.next=nn
            nn.prev=fn
            fn=nn      
    def display(self):

        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,end='')
                if temp.next!=None:
                    print("<->",end='')
                else:
                    print("")
                temp=temp.next
                

obj=doublell()
# n=node(10)
# obj.head=n
# n1=node(20)
# n.next=n1
# n1.prev=n
# n2=node(30)
# n1.next=n2
# n.prev=n1
# obj.insbeg(5)
n=int(input())
fn=int(input())

obj.userip(n,fn)
obj.inbtw(4,2)
obj.inslast(7)
obj.display()

