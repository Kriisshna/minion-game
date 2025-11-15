# create a single linked list counting of 2 total number of 6. insert nodes 10 20 30 at the beginning 
# \constrains: create two sepearate functions for insertion at beginning and end
# series 2,4,6,8,10,12
# user input beg and end


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlell:
    def __init__(self):                                         
        self.head=None
    def insbeg(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb
    def inslast(self,data):
        n=node(data)
        temp=self.head
        while (temp.next):
            temp=temp.next
        temp.next=n
    def inbtw(self,data,p):
        nbtw=node(data)
        temp=self.head
        for i in range(p-2):
            temp=temp.next
        nbtw.next=temp.next
        temp.next=nbtw
    def dlt(self):
        self.head=self.head.next

    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"->",end='')
                temp=temp.next

obj=singlell()
obj.head=node(2)
i=obj.head

for j in range(2,7):
    i.next=node(j*2)
    i=i.next
# obj.display()
n=int(input())
# for i in range(n):
#     x=int(input())
#     obj.insbeg(x)
# n=int(input())

for i in range(n):
    x=int(input())
    p=int(input())
    obj.inbtw(x,p)
# obj.inbtw(553)

# obj.dlt()
# obj.inbtw(5,3)
obj.display()
