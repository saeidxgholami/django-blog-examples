print('hello world!')

class Person:
    def __init__(self, name):
        self.name = name

p = Person('John Doe')
print(p.name)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Hello Tk!')

name = ttk.Entry(root)
age = ttk.Entry(root)

name.grid(row=0, column=0)
age.grid(row=1, column=0)

cancel = ttk.Button(root, text="Cancel")
ok = ttk.Button(root, text="OK")
cancel.grid(row=2, column=0)
ok.grid(row=3, column=1)



root.mainloop()