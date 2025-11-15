class encap:
    _a=10
    print(_a)
    def encapfn(self):
        print("ds")
        print(self._a)
obj=encap()
obj.encapfn()
print(obj._a)