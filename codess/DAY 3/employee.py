class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print(self.name,self.id)
        print(f"hi my name is {self.name}.My id is {self.id}")
emp1=employee("rei",123)
emp1.display()        
emp2=employee("rei2",45945)
emp2.display()

