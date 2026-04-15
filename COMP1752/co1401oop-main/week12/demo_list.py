from tkinter import *   
from tkinter import messagebox as mb
from tkinter import filedialog
from student import Student

from gui_base import GUIBase
import csv

class StudentListApp(GUIBase):
    def __init__(self):
        super().__init__(title="Student List", width=555, height=450)

        self._students_list = []  # empty list to hold student objects

    def _create_widgets(self):
        lbl_title = Label(self._window, text="Student List")
        lbl_title.grid(row=0, column=0, padx=5, pady=5, columnspan=6, sticky=EW)

        lbl_search = Label(self._window, text="Search:")
        lbl_search.grid(row=1, column=0, padx=5, pady=5, sticky=W)


        self.search_var = StringVar()
        txt_search = Entry(self._window, textvariable=self.search_var)
        txt_search.grid(row=1, column=1, padx=5, pady=5, sticky=E)

        self.lst_students = Listbox(self._window, width=30, height=15, selectmode=SINGLE, exportselection=False)
        self.lst_students.grid(row=2, column=0, columnspan=2, rowspan=4, padx=5, pady=5, sticky=W)
        # bind selection event to the listbox
        self.lst_students.bind('<<ListboxSelect>>', self.lst_students_selected)

        btn_import = Button(self._window, text="Import", command=self.btn_import_clicked)
        btn_import.grid(row=6, column=0, padx=5, pady=5, sticky=W)

        btn_export = Button(self._window, text="Export", command=self.btn_export_clicked)
        btn_export.grid(row=6, column=1, padx=5, pady=5, sticky=E)

        lbl_id = Label(self._window, text="ID:")
        lbl_id.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        self.id_var = StringVar()
        txt_id = Entry(self._window, textvariable=self.id_var)
        txt_id.grid(row=2, column=3, padx=5, pady=5, columnspan=3, sticky=E)
        # bind Enter key to search function
        txt_search.bind('<Return>', lambda event: self.search_by_name())

        lbl_name = Label(self._window, text="Name:")
        lbl_name.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        self.name_var = StringVar()
        txt_name = Entry(self._window, textvariable=self.name_var)
        txt_name.grid(row=3, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        lbl_age = Label(self._window, text="Age:")
        lbl_age.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        self.age_var = StringVar()
        txt_age = Entry(self._window, textvariable=self.age_var)
        txt_age.grid(row=4, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        lbl_gpa = Label(self._window, text="GPA:")
        lbl_gpa.grid(row=5, column=2, padx=5, pady=5, sticky=W)

        self.gpa_var = StringVar()
        txt_gpa = Entry(self._window, textvariable=self.gpa_var)
        txt_gpa.grid(row=5, column=3, padx=5, pady=5, columnspan=3, sticky=E)

        btn_add = Button(self._window, text="Add", command=self.btn_add_clicked)
        btn_add.grid(row=6, column=3, padx=5, pady=5, sticky=W)

        btn_save = Button(self._window, text="Save", command=self.btn_save_clicked)
        btn_save.grid(row=6, column=4, padx=5, pady=5, sticky=E)

        btn_del = Button(self._window, text="Del", command=self.btn_del_clicked)
        btn_del.grid(row=6, column=5, padx=5, pady=5, sticky=E)

    def btn_import_clicked(self):
        # open file dialog to select a CSV file
        file_csv = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
        if file_csv:
            try:
                with open(file_csv, newline='') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)  # Skip the header row
                    for row in reader:
                        id, name, age, gpa = row
                        student = Student(id, name, int(age), float(gpa))
                        self._students_list.append(student)         # add student object to the list
                        self.lst_students.insert(END, str(student)) # add student's string to the listbox
            except Exception as e:
                mb.showerror("Error", f"Failed to import CSV: {e}")
        else:
            mb.showinfo("Cancelled", "Import cancelled")

    def lst_students_selected(self, event):
        # get selected index
        selected_index = self.lst_students.curselection()[0] # list allows multiple selection, get the first one
        selected_student = self._students_list[selected_index]
        # update student details in the entry fields
        self.id_var.set(selected_student._id)
        self.name_var.set(selected_student._name)
        self.age_var.set(selected_student._age)
        self.gpa_var.set(selected_student._gpa)

    def btn_add_clicked(self):
        # get student details from entry fields
        id = self.id_var.get()
        name = self.name_var.get()
        age = self.age_var.get()
        gpa = self.gpa_var.get()
        # add to list and listbox
        student = Student(id, name, int(age), float(gpa))
        self._students_list.append(student)         # add student object to the list
        self.lst_students.insert(END, str(student)) # add student's string to the listbox
        # show success message
        mb.showinfo("Success", f"Student {name} added successfully!")

    def btn_del_clicked(self):
        try:
            selected_index = self.lst_students.curselection()[0] # list allows multiple selection
            selected_student = self._students_list[selected_index]
            # remove from list and listbox
            del self._students_list[selected_index] # remove student object from the list
            self.lst_students.delete(selected_index) # remove student string from the listbox
            # show success message
            mb.showinfo("Success", f"Student {selected_student._name} deleted successfully!")
        except IndexError:
            mb.showerror("Error", "No student selected to delete")
            return

    def btn_save_clicked(self):
        try:
            # get selected index
            selected_index = self.lst_students.curselection()[0] # list allows multiple selection
            selected_student = self._students_list[selected_index]
            # update student details from entry fields
            selected_student._id = self.id_var.get()
            selected_student._name = self.name_var.get()
            selected_student._age = int(self.age_var.get())
            selected_student._gpa = float(self.gpa_var.get())
            # update listbox display
            self.lst_students.delete(selected_index) # remove old entry
            self.lst_students.insert(selected_index, str(selected_student)) # insert updated entry

            mb.showinfo("Success", f"Student {selected_student._name} updated successfully!")
        except IndexError:
            mb.showerror("Error", "No student selected to save")
            return
        except ValueError:
            mb.showerror("Error", "Invalid age or GPA value")
            return

    def btn_export_clicked(self):
        file_csv = filedialog.asksaveasfilename(title="Save CSV file", defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_csv:
            mb.showinfo("Cancelled", "Export cancelled")
            return
        
        try:
            with open(file_csv, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["ID", "Name", "Age", "GPA"]) # write header
                for student in self._students_list:
                    writer.writerow([student._id, student._name, student._age, student._gpa]) # write student details
            mb.showinfo("Success", f"Student list exported successfully to {file_csv}")
        except Exception as e:
            mb.showerror("Error", f"Failed to export CSV: {e}")

    def search_by_name(self):
        name = self.search_var.get()

        for st in self._students_list:
            if st._name == name:
                self.id_var.set(st._id)
                self.name_var.set(st._name)
                self.age_var.set(st._age)
                self.gpa_var.set(st._gpa)
                return
        
        mb.showinfo("Not found", f"No student found with name {name}")

if __name__ == "__main__":
    app = StudentListApp()
    app.run()