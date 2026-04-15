from tkinter import *   
from tkinter import messagebox as mb

class MyApp03:
    def __init__(self):
        # create the main window
        self.window = Tk()
        self.window.title("My GUI App 03")
        self.window.geometry("400x300")

        # create widgets
        lbl_firstname = Label(self.window, text="First Name:")
        lbl_firstname.grid(row=0, column=0)

        self.var_firstname = StringVar()   # create a StringVar to hold the value of the first name entry
        txt_firstname = Entry(self.window, textvariable=self.var_firstname) # bind the entry to the StringVar
        txt_firstname.grid(row=0, column=1)

        lbl_lastname = Label(self.window, text="Last Name:")
        lbl_lastname.grid(row=1, column=0)

        self.var_lastname = StringVar()   # create a StringVar to hold the value of the last name entry
        txt_lastname = Entry(self.window, textvariable=self.var_lastname) # bind the entry to the StringVar
        txt_lastname.grid(row=1, column=1)

        btn_hello = Button(self.window, text="Hello", command=self.btn_hello_clicked)
        btn_hello.grid(row=2, column=0)

        self.var_fullname = StringVar()   
        txt_fullname = Entry(self.window, textvariable=self.var_fullname) 
        txt_fullname.grid(row=2, column=1)
    
    def btn_hello_clicked(self):
        # get first name and last name from the entry widgets
        firstname = self.var_firstname.get()   # get the value of the first name entry
        lastname = self.var_lastname.get()     # get the value of the last name entry
        fullname = f"Hi, {firstname} {lastname}"   # concatenate first name and last name to
        self.var_fullname.set(fullname)    # set the value of the full name entry to the concatenated string

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MyApp03()
    app.run()