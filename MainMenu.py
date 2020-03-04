from tkinter import *

root = Tk()
root.title("Contacts")
root.geometry("500x250")

main_menu = Menu()
file_menu = Menu(font=("Times New Roman", 12, "bold"), tearoff=0)
main_menu = Menu()
main_menu.add_cascade(label="Create")
main_menu.add_cascade(label="Find")
main_menu.add_cascade(label="Edit")
main_menu.add_cascade(label="Delete")
main_menu.add_cascade(label="Exit")

root.config(menu=main_menu)
root.mainloop()


