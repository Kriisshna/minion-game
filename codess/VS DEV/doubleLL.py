class node():
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None

class doubleLL():
    def __init__(self):
        self.head=None

    def insertb(self,data):
        new=node(data)
        temp=self.head
        new.next=temp
        temp.prev=new
        self.head=new
        
    def inserte(self,data):
        ne=node(data)
        t=self.head
        while(t.next):
            t=t.next
        t.next=ne
        ne.prev=t.next

    # def position()

    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"<-->",end=" ")
                temp=temp.next 

obj=doubleLL()
n=node(20)
obj.head=n
n1=node(10)
n.next=n1
n1.prev=n
n2=node(300)
n1.next=n2
n2.prev=n1
n3=node(105)
n2.next=n3
n3.prev=n2
obj.insertb(1044)
obj.inserte(234)
obj.display()