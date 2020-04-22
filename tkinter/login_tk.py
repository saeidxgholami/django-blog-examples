import tkinter as tk

from tkinter import ttk



def main():
	root = tk.Tk()
	root.title("login")
	mainframe = ttk.Frame(root)
	mainframe.pack()

	ttk.Label(mainframe, text="Username: ").grid(row=0, column=0)
	ttk.Label(mainframe, text="Password: ").grid(row=1, column=0)
	name = ttk.Entry(mainframe)
	password = ttk.Entry(mainframe)
	name.grid(row=0, column=1)
	password.grid(row=1, column=1)
	login = ttk.Button(mainframe, text="Login")
	cancel = ttk.Button(mainframe, text="Cancel")
	login.grid(row=2, column=1, sticky='w')
	cancel.grid(row=2, column=1, sticky='e')

	for child in mainframe.winfo_children():
		child.grid_configure(padx=5, pady=5)

		
	root.mainloop()


if __name__ == "__main__":
	main()