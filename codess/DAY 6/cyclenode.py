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
        for _ in range(1,n):
            new=int(input())
            nn=node(new)
            fn.next=nn
            fn=nn
    def cycle(self,p):
        tempc=self.head
        while(tempc.next):
            tempc=tempc.next
        start=self.head
        for _ in range(p-1):
            start=start.next        
        tempc.next=start

    def alg(self):
        slowp=self.head
        fastp=self.head
        while (True):
            slowp=slowp.next
            fastp=fastp.next.next
            if fastp==slowp:
                break
        fastp=self.head
        while (True):
            slowp=slowp.next
            fastp=fastp.next
            if fastp==slowp:
                break
        
        print(fastp.data)

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            for _ in range(n+1) :
                print(temp.data,end="")
                
                
                temp=temp.next
                if temp.next!=None:
                    print("->",end='')
                else:
                    print("")
obj=singlell()
n=int(input())
fd=int(input())
obj.userip(n,fd)
obj.cycle(3)
obj.alg()
obj.display()


