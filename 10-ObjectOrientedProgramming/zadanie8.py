<<<<<<< HEAD
class Telephone():
    def __init__(self, brand, model, year, battery):
        self.brand = brand
        self.model = model
        self.year = year
        self.battery_level = battery
        self.is_on = True
        self.notifications = 0
    def notification(self,i):
        self.notifications = i
=======
'''
8.	Identify at least 3 states and 3 behaviors for a telephone
object. Then, for the listed states and behaviors, 
create a class with fields (attributes) and methods. 
Try to use verbs in method names as they describe activities. 
Finally, create a object, call its methods and display object’s 
properties.
'''

class Telephone():
    def __init__(self, brand, model, year, battery_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.battery_level = battery_level
        self.is_on = True
        self.number_of_notifications = 0
    def notification(self):
        self.number_of_notifications += 1
        print("You have new notification. Current number of notifications: ", self.number_of_notifications)
>>>>>>> 9483540570fe22877102a16b9b29a47e140612f9
    def off(self):
        self.is_on = False
    def charged(self):
        self.battery_level = 100
<<<<<<< HEAD

my_phone = Telephone("Oppo", "A96", 2023, 100)

my_phone.notification(7)
my_phone.off
my_phone.charged

print(my_phone.battery_level)
print(my_phone.notifications)
=======
        print(f"The phone is charged! Battery level is {self.battery_level}")
        

my_phone = Telephone("Abcd", "1234", 2024, 46)

my_phone.charged()
my_phone.notification()
my_phone.notification()
my_phone.notification()
my_phone.off()

print(f"{my_phone.brand} {my_phone.model} year of production is {my_phone.year}")
print(f"Phone is on: {my_phone.is_on}")
>>>>>>> 9483540570fe22877102a16b9b29a47e140612f9
