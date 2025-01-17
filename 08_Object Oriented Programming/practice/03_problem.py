# create a class with a class attribute a; create an object from it and set 'a' directly using object.a=0. 
# Does this change the class attribute?

class clas:
    a=10
obj=clas()
obj.a=1
print(obj.a)
objj=clas()
print(objj.a)
