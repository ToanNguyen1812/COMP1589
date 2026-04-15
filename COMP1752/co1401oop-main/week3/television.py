class Television:
    def __init__(self):
        self.status = False  # TV is initially off
        self.channels = ['BBC', 'CNN', 'Discovery', 'National Geographic']
        self.current_channel = 0    # 0 means the first channel in the list ('BBC')

    def turn_on(self):
        self.status = True
        self.display()

    def display(self):
        if not self.status:
            print("The television is OFF")
            return
        
        print(f"TV is playing {self.channels[self.current_channel]} channel")

    def turn_off(self):
        self.status = False
        self.display()

    def switch_channel(self, new_channel: int):
        # validation
        if new_channel not in range(len(self.channels)):
            print("Invalid channel number")
            return
        # main logic
        self.current_channel = new_channel
        self.display()

if __name__ == "__main__":
    print("Testing Television class")
    tv = Television()
    tv.display()
    tv.turn_on()
    tv.switch_channel(2)
    tv.switch_channel(4)  # invalid channel
    tv.turn_off()