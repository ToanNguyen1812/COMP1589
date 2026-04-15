class Student:
    def __init__(self, id, name, age, gpa):
        self._id = id
        self._name = name
        self._age = age
        self._gpa = gpa

    def __str__(self):
        return f"{self._id} - {self._name}"