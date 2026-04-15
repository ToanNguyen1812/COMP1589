from tkinter import *   # import all the functions and classes from the tkinter module
from tkinter import messagebox as mb   # import the messagebox module from tkinter and give it an alias 'mb'

class MyApp:
    def __init__(self):
        # create the main window
        self.window = Tk()   # create a new instance of the Tk class
        self.window.title("My First GUI")   # set the title of the window
        self.window.geometry("400x300")   # set the size of the window (width x height)

        # add a label to the window
        self.label = Label(self.window, text="Hello, World!")
        self.label.grid(row=0, column=0)   # place the label in the grid at row 0, column 0

        # add a button to the window, register the event handler for the button click event
        self.button = Button(self.window, text="Click Me!", command=self.button_clicked)   
        self.button.grid(row=1, column=0)   # place the button in the grid at row 1, column 0
    
    # event handler for button click
    def button_clicked(self):
        mb.showinfo("Button Clicked", "You clicked the button!")  # showinfo(title, message)

    def run(self):
        self.window.mainloop()   # start the main event loop to display the window and wait for user interactions

if __name__ == "__main__":
    app = MyApp()
    app.run()