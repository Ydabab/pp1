class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            try:
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no]})")
            except:
                print(f"TV in on, channel {self.channel_no}")
        else:
            print("TV is off")
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
    def set_channels(self, channels_list):
        for i in channels_list:
            self.channels.append(i)
    def show_channels(self):
        counter = 1
        for i in self.channels:
            print(f"{counter}. {i}")
            counter += 1        

tv_set = TV()
tv_set.show_status()
tv_set.turn_on()
tv_set.show_status()
tv_set.show_channels()
tv_set.set_channels(["TVP1","TVP2","TVP3 Kraków","Polsat","TVN","Filmbox","Discovery"])
tv_set.show_channels()
tv_set.set_channel(4)
tv_set.show_status()
tv_set.set_channel(99)
tv_set.show_status()
tv_set.turn_off()
