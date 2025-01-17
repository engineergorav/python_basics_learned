class employ:
    name="gorav" #this is a class atribute
    language="py"
# it is also known as dunder method
    def __init__(self):# this fun will called automatically when an object is made of this class

        print(f"an object is made {self.name}  ")


    def get_info(self):

        print(f"the language of {self.name} is {self.language} \nhis salary is {self.salary}")


    @staticmethod
    def greet():
        print("good morning!\n")

object=employ()
object.salary="7,00,00,000" # this is an instance/object atribute
object.greet()
employ.get_info(object)
a=employ()