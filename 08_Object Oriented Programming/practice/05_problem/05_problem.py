#  write a class train which has methods to book a ticket,get status (no seats availabe ) 
# and get fair information of train running under Indian Railway
from random import randint
class Train:
    def book_ticket(self,train_no,place_1,place_2):
        print(f"ticket is booked of train number {self.train_no}\nfrom {self.place_1} to {self.place_2}")
    def get_status(self,ticket_no):
        print(f"the  train number {self.train_no} is booked successfullt from {self.place_1} to {self.place_2}")
        pass
    def get_fair(self,train_no,place_1,place_2):
        print(f"ticket fair of train number {self.train_no}\nfrom {self.place_1} to {self.place_2} is {randint(500,1000)}")
obj=Train(1234567890,"Nangal","Delhi")
print(obj.book_ticket())
