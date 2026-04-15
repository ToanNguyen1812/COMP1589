class LightBulb:
    def __init__(self):
        self.status = False  # Light bulb is initially off
        self.color = 'White'  # Default color

    def display(self):
        if not self.status:
            print("The light bulb is OFF")
        else:
            print(f"The light bulb is ON with color {self.color}")

    def turn_on(self):
        self.status = True
        self.display()

    def turn_off(self):
        self.status = False
        self.display()

    def switch_color(self):
        if self.color == 'White':
            self.color = 'Cool White'
        elif self.color == 'Cool White':
            self.color = 'Yellow'
        else:
            self.color = 'White'

        self.display()

## Test this class
if __name__ == "__main__":
    print("Testing LightBulb class")
    bulb = LightBulb()
    bulb.display()
    print('-*' * 20)
    bulb.turn_on()
    print('-*' * 20)
    bulb.switch_color()
    print('-*' * 20)
    bulb.switch_color()
    print('-*' * 20)
    bulb.switch_color()