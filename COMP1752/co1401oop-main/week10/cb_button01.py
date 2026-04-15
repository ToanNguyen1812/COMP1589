from tkinter import *   
from tkinter import messagebox as mb

from gui_base import GUIBase

class DemoCheckbox(GUIBase):
    def __init__(self, title="Demo Checkbox", width=400, height=300):
        super().__init__(title, width, height)

    def _create_widgets(self):
        lbl_prompt = Label(self._window, text='Select languages you can speak:')
        lbl_prompt.grid(row=0, column=0, padx=10, pady=10)

        self.english_var = BooleanVar()
        chk_english = Checkbutton(self._window, text="English", variable=self.english_var)
        chk_english.grid(row=1, column=0, sticky=W, padx=20)

        self.french_var = BooleanVar()
        chk_french = Checkbutton(self._window, text="French", variable=self.french_var)
        chk_french.grid(row=2, column=0, sticky=W, padx=20)

        self.spanish_var = BooleanVar()
        chk_spanish = Checkbutton(self._window, text="Spanish", variable=self.spanish_var)
        chk_spanish.grid(row=3, column=0, sticky=W, padx=20)

        btn_confirm = Button(self._window, text="Confirm", command=self.btn_confirm_clicked)
        btn_confirm.grid(row=4, column=0, pady=20)

    def btn_confirm_clicked(self):
        languages = []
        if self.english_var.get() == True:
            languages.append("English")
        if self.french_var.get() == True:
            languages.append("French")
        if self.spanish_var.get() == True:
            languages.append("Spanish")
        
        if len(languages) > 0:
            mb.showinfo("Selected Languages", "I can speak: " + ", ".join(languages))
        else:
            mb.showinfo("Selected Languages", "I cannot speak any language.")
if __name__ == "__main__":
    app = DemoCheckbox()
    app.run()