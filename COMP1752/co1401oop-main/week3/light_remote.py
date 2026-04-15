# syntax to import a moduel: from file_name import class_name, function_name

from light_bulb import LightBulb

class LightRemote:
    def __init__(self, bulb: LightBulb):
        self.bulb = bulb

    def press(self, long_press=False):
        if long_press:
            self.bulb.turn_off()
            return
        
        if self.bulb.status == False:   # light is off, turn it on
            self.bulb.turn_on()
        else:
            self.bulb.switch_color()    # light is on, switch color

if __name__ == "__main__":
    # create a LightBulb object
    bulb = LightBulb()
    # create a LightRemote object to control the bulb
    remote = LightRemote(bulb)
    # test the remote
    remote.press()          # press to turn on
    print('-*' * 20)
    remote.press()          # press to switch color
    print('-*' * 20)
    remote.press()          # press to switch color
    print('-*' * 20)
    remote.press()          # press to switch color
    print('-*' * 20)
    remote.press(long_press=True)  # long press to turn off