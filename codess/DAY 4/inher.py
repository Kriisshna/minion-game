class parent:
    def __init__(self):
        self.x=100
    def one(self):
        print("yo")
class child(parent):
    def two(self):
        print(self.x)   
     
obj=child()
obj.two()

