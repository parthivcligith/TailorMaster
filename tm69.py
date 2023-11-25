from cProfile import label
from tkinter import *
#window
root= Tk()
#title
root.title("Taylormaster69")
#icon
root.iconbitmap("measuring.ico")
#window size
root.geometry("800x600")
#label
name_label=Label(root,text="Name : ")
phone_label=Label(root,text="Phnone : ")
address_label=Label(root,text="Address : ")
#layout of label
name_label.grid(row=0,column=0)
phone_label.grid(row=1,column=0)
address_label.grid(row=2,column=0)


root.mainloop()