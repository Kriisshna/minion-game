class a:
    def __init__(self):
        self._x=100
    def one(self):
        print("ok")

class b:
    def two(self):
        print("child")
        print(self._x)

j=b()
j.two()
j.one()