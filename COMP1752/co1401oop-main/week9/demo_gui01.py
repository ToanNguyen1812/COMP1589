from gui_base import GUIBase
from tkinter import *   
from tkinter import messagebox as mb

class MyGUI(GUIBase):
    def __init__(self):
        super().__init__("Demo GUI 01")

    def create_widgets(self):
        self.label = Label(self.window, text="Hello, World!")
        self.label.grid(row=0, column=0)

        self.button = Button(self.window, text="Click Me", command=self.on_button_click)
        self.button.grid(row=1, column=0)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

if __name__ == "__main__":
    app = MyGUI()
    app.run()