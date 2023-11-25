from tkinter import *
from PIL import Image, ImageGrab,ImageTk
from tkinter.font import Font
import pyautogui
import win32com
import win32print
import win32ui

root1=Tk()
root1.title("items")
root1.geometry("770x600")
root1.iconbitmap("Icons8-Ios7-Clothing-Hanger.ico")
root1.configure(background="#fefefe")

my_font = Font(
        family = 'Times',
        size = 18,
        weight = 'bold',
        slant = 'roman',
        underline = 0,
        overstrike = 0,
    )

image = Image.open("shirtt.jpg")

width, height = image.size
new_width = 1500
new_height = int((float(height) / width) * new_width)
image = image.resize((new_width, new_height))

tk_image = ImageTk.PhotoImage(image)

label = Label(root1, image=tk_image)
label.place(x=-390, y=-390)



Label(root1,text="Measurements",font=my_font,fg="#45496A").place(x=290,y=10)

entry1 = Entry(root1,background="#FDF4F3",width=4)
entry1.place(x=268,y=128)

entry2 = Entry(root1,background="#FDF4F3",width=4)
entry2.place(x=70,y=158)

entry3 = Entry(root1,background="#FDF4F3",width=4)
entry3.place(x=85,y=265)

entry4 = Entry(root1,background="#FDF4F3",width=4)
entry4.place(x=312,y=257)

entry5 = Entry(root1,background="#FDF4F3",width=4)
entry5.place(x=308,y=327)

entry6 = Entry(root1,background="#FDF4F3",width=4)
entry6.place(x=295,y=398)

entry7 = Entry(root1,background="#FDF4F3",width=4)
entry7.place(x=369,y=450)

entry8 = Entry(root1,background="#FDF4F3",width=4)
entry8.place(x=392,y=155)

entry9 = Entry(root1,background="#FDF4F3",width=4)
entry9.place(x=502,y=283)

def ss():
    # Get the coordinates of the window
    x = root1.winfo_rootx()
    y = root1.winfo_rooty()
    w = root1.winfo_width()
    h = root1.winfo_height()

    # Take the screenshot
    h=h-90
    image = ImageGrab.grab(bbox=(x, y, x+w, y+h))

    # Save the screenshot to a file
    image.save("screenshot.png")
    
    """photo = ImageTk.PhotoImage(image)
    label = Label(root1, image=photo)
    label.pack()"""

Button(root1,text="PRINT",width=15,background="#F8D6DD", command=ss).place(x=599,y=530)
Button(root1,text="SUBMIT",width=15,background="#F8D6DD").place(x=320,y=530)

root1.mainloop()
