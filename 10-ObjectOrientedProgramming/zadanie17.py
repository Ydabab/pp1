class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
        #włączenie
    def turn_off(self):
        self.is_on = False
        #wyłączenie
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        #zmiana kanału
    def set_channels(self, channels_list):
        for i in channels_list:
            self.channels.append(i)
        #zaprogramowanie listy kanałów
    def show_channels(self):
        counter = 1
        for i in self.channels:
            print(f"{counter}. {i}")
            counter += 1
        #wyświetlenie listy kanałów
    def show_status(self):
        if self.is_on == True:
            try:
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no]}) Volume: {self.volume}")
            except:
                print(f"TV in on, channel {self.channel_no} Volume: {self.volume}")
        else:
            print("TV is off")
        #wyświeltenie statusu(czy włączony, kanał i nazwa kanału)
    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

tv_set = TV()
tv_set.show_status()
tv_set.turn_on()
tv_set.show_status()
tv_set.volume_up()
tv_set.volume_up()
tv_set.show_status()
tv_set.volume_down()
tv_set.show_status()