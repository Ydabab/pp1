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
    def off(self):
        self.is_on = False
    def charged(self):
        self.battery_level = 100

my_phone = Telephone("Oppo", "A96", 2023, 100)

my_phone.notification(7)
my_phone.off
my_phone.charged

print(my_phone.battery_level)
print(my_phone.notifications)