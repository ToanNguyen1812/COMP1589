from tkinter import *   # import all the functions and classes from the tkinter module
from tkinter import messagebox as mb   # import the messagebox module from tkinter and give it an alias 'mb'
# event handlers

def button_clicked():
    mb.showinfo("Button Clicked", "You clicked the button!")  # showinfo(title, message)

# create the main window
window = Tk()   # create a new instance of the Tk class
window.title("My First GUI")   # set the title of the window
window.geometry("400x300")   # set the size of the window (width x height)

# add a label to the window
label = Label(window, text="Hello, World!")
label.grid(row=0, column=0)   # place the label in the grid at row 0, column 0

# add a button to the window, register the event handler for the button click event
button = Button(window, text="Click Me!", command=button_clicked)   # create a button with the text "Click Me!" and set its command to the button_clicked function
button.grid(row=1, column=0)   # place the button in the grid at row 1, column 0

window.mainloop()   # start the main event loop to display the window and wait for user interactions