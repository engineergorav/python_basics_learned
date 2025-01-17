# Create a class (pet) from a class (animal) and further create a class (dog) from pet. 
# Add a "bark" method to (dog)


class Animal:
    pass
class Pet(Animal):
    pass
class Dog(Pet):
    @staticmethod
    def Bark():
        return("bhoww bhoww")
a=Animal()
b=Pet()
c=Dog()
print(c.Bark())