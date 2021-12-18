from tkinter import *
from tkinter import ttk

class dialog:
    name = ""
    people = ['abc', 'def', 'ghi']

    def __init__(self, people):
        self.people = people

    def set_person(self, person, root):
        self.name = person
        root.destroy()

    def show_dialog(self):
        btns = []
        root = Tk("multiple people detected!")
        frm = ttk.Frame(root, padding=10)
        frm.grid()
        ttk.Label(frm, text="Multiple faces detected").grid(column=0, row=0)
        ttk.Label(frm, text="Which person's video do you wanna play?").grid(column=0, row=1)
        i = 2
        for j in range(len(self.people)):
            btns.append(ttk.Button(frm, text=self.people[i], command=lambda: self.set_person(self.people[j], root)).grid(column=0, row=i))
            i += 1
            btns[j].pack()


        ttk.Button(frm, text="Quit, dont play any videos", command=root.destroy).grid(column=0, row=i)
        root.mainloop()

d = dialog(['a', 'f', 'd'])
d.show_dialog()
print(d.name)


