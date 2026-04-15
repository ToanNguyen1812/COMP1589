from tkinter import *   
from tkinter import messagebox as mb
from abc import ABC, abstractmethod

class GUIBase(ABC):
    def __init__(self, title="My GUI App", width=400, height=300):
        self.create_window(title, width, height)
        self.create_widgets()

    def create_window(self, title, width, height):  
        self.window = Tk()
        self.window.title(title)
        self.window.geometry(f"{width}x{height}")

    @abstractmethod
    def create_widgets(self):
        pass

    def run(self):
        self.window.mainloop()