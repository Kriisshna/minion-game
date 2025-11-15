class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singleLL:
    def __init__(self):
        self.head=None

    def createcyc(self,p):
        temp=self.head
        while(temp.next):
            temp=temp.next
        start=self.head   
        for _ in range(p-1):
            start=start.next 
        temp.next=start
    
    def detection(self):
        fast=self.head
        slow=self.head
        while(True):
            fast=fast.next.next
            slow=slow.next
            if(fast==slow):
                break

        fast=self.head
        while(True):
            fast=fast.next
            slow=slow.next
            if(fast==slow):
                break
        print("the start of cycle is",fast.data)

    def display(self,n):
        if self.head is None:
            print("no elements")
        else:
            temp=self.head
            for _ in range (n+1):
                print(temp.data,end=" ")
                
                if temp.next!=None:
                    print("->",end="")
                else:
                    print("")
                temp=temp.next
obj=singleLL()
n=int(input())
fd=node(input())
obj.head=fd
for _ in range (1,n):
    new=int(input())
    nn=node(new)
    fd.next=nn
    fd=nn
obj.createcyc(2)
obj.detection()
obj.display(n)