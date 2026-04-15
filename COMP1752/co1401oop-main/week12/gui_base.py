from tkinter import *   
from tkinter import messagebox as mb
from abc import ABC, abstractmethod

class GUIBase(ABC):
    def __init__(self, title="My GUI App", width=400, height=300):
        self.__create_window(title, width, height)
        self._create_widgets()

    def __create_window(self, title, width, height):  
        self._window = Tk()                         # _window is a protected attribute, accessible in subclasses
        self._window.title(title)
        self._window.geometry(f"{width}x{height}")

    @abstractmethod
    def _create_widgets(self):
        pass

    def run(self):
        self._window.mainloop()