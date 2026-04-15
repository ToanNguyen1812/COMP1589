from tkinter import *   
from tkinter import messagebox as mb

from gui_base import GUIBase

class DemoRadio(GUIBase):
    def __init__(self, title="Demo Radio Buttons", width=400, height=300):
        super().__init__(title, width, height)

    def _create_widgets(self):
        lbl_prompt = Label(self._window, text="What language can you speak:")
        lbl_prompt.grid(row=0, column=0, padx=10, pady=10)

        self.language_var = IntVar()  # Default value
        self.language_var.set(1)  # Set default to English

        rd_english = Radiobutton(self._window, text="English", variable=self.language_var, value=1)
        rd_english.grid(row=1, column=0, sticky=W, padx=20)

        rd_french = Radiobutton(self._window, text="French", variable=self.language_var, value=2)
        rd_french.grid(row=2, column=0, sticky=W, padx=20)

        rd_spanish = Radiobutton(self._window, text="Spanish", variable=self.language_var, value=3)
        rd_spanish.grid(row=3, column=0, sticky=W, padx=20)

        btn_confirm = Button(self._window, text="Confirm", command=self.btn_confirm_clicked)
        btn_confirm.grid(row=4, column=0, pady=20)
    # event handler
    def btn_confirm_clicked(self):
        # get the selected language 
        selected_language = self.language_var.get()
        
        if selected_language == 1:
            language = "English"
        elif selected_language == 2:
            language = "French"
        else:
            language = "Spanish"

        mb.showinfo("Selected Language", f"I can speak: {language}")

if __name__ == "__main__":
    app = DemoRadio()
    app.run()