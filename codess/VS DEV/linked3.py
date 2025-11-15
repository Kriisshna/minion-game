"""
create single LL with counting of two's total number of elemets = 6
2→→>4-→>6→>8->10→>12
inert nodes 10,20,30 at the begining
exp 0/p:- 10→> 20→> 30→> 2->4→>6->8→>10->12
also insert 555 as last node
exp 0/p: - 10→→ 20→→> 30→→> 2→→>4->6→>8→>10—>12—>55

"""

class node:
    def __init__(self,data):
        self.data= data
        self.next= None

class singlell:
    def __init__(self):
        self.head= None

    def insertb(self,data):
        nb=node(data)
        nb.next=self.head
        self.head=nb

    def inserte(self,data):
        ne=node(data)
        emp=self.head
        while(emp.next):
            emp=emp.next
        emp.next=ne

        

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"->",end=" ")
                temp=temp.next

obj=singlell()
obj.head=node(2)
heado=obj.head

for i in range (2,7):
    heado.next=node(i*2)
    heado=heado.next

#inputs for insert at start
# n=int(input("no: of values to be inserted:"))
# for _ in range (n):
#     x=input()
#     obj.insertb(x)
# obj.inserte(555)
# obj.display()

#p=int(input("insertion position:"))
obj.head=heado.next
obj.display()