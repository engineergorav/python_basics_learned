class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
    def showw(cls):
        print(f"The instance attribut is {cls.a}")
o=Employee()
o.a=2
o.show()
o.showw()