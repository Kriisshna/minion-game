class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlell:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"->",end='')
                temp=temp.next
obj=singlell()
n=node(10)
obj.head=n
n1=node(20)
obj.head.next=n1
n2=node(30)
n1.next=n2
obj.display()