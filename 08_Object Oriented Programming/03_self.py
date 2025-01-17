class employ:
    name="gorav" #this is a class atribute
    language="py"
    def get_info(self):
        print(f"the language of {self.name} is {self.language} and salary is {self.salary}")

object=employ()
object.salary=120000 # this is an instance/object atribute
# object.get_info()
employ.get_info(object)