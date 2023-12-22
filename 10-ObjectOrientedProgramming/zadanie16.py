class Phone():
    def __init__(self):
        self.is_on = False
        self.charging = False
        self.ringing = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False

myphone = Phone()

print(myphone.is_on)
myphone.turn_on()
print(myphone.is_on)
myphone.turn_off()
print(myphone.is_on)