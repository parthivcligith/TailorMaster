from distutils.util import execute
from msilib.schema import ComboBox, RadioButton
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Style
from turtle import shape
import mysql.connector
from tkinter.font import Font
from PIL import Image,ImageTk

 
 
#combobox function
def cb(event):
    root1=Toplevel(root)
    root1.title("items")
    root1.geometry("770x600")
    root1.iconbitmap("Icons8-Ios7-Clothing-Hanger.ico")
    
    image = Image.open("shirtt.jpeg")

    width, height = image.size
    new_width = 550
    new_height = int((float(height) / width) * new_width)
    image = image.resize((new_width, new_height))

    tk_image = ImageTk.PhotoImage(image)

    label = Label(root1, image=tk_image)
    label.place(x=110, y=90)

    Entry(root1).place(x=100,y=50)

    root1.mainloop()





#radiobutton function

def rb():
    a=v.get()
    if (a==1):
        n=StringVar(root)
        item=['Shirt','Pants','coat']
        item=Combobox(root,textvariable=n,width=12,height=1,values=item)
        item.current(1)
        item.place(x=540,y=390)
        item.bind("<<ComboboxSelected>>",cb)
                
        Label(root,text="Choose item :",fg="#800709",background="#f3d6cd").place(x=450,y=390) 

    else:
        n=StringVar(root)
        item=Combobox(root,textvariable=n,width=12,height=1)
        item['values']=('Churidar','Blouse','Kurti')
        item.place(x=540,y=390)
        Label(root,text="Choose item :",fg="#800709",background="#f3d6cd").place(x=450,y=390) 
        




#button click - database 

def Ok():
    id = e1.get()
    name=e2.get()
    phn = e3.get()
    mail = e4.get()
 
    #db connect
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="Parthiv@3427",database="demodb")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO customertable (id,cname,cphn,cmail,date) VALUES (%s, %s, %s, %s,curdate())"
       val = (id,name,phn,mail)
       mycursor.execute(sql, val)
       mysqldb.commit()
       
       messagebox.showinfo("information", "Record inserted successfully...")
       
       #e.insert(0,e1+1)
       show()

 
    except Exception as e:
 
       messagebox.showinfo("ERROR",e)
       mysqldb.rollback()
       mysqldb.close()

def show():
    my_connect = mysql.connector.connect(
    host="localhost",
    user="root", 
    passwd="Parthiv@3427",
    database="demodb"
)
    my_conn = my_connect.cursor()
####### end of connection endi ####
    my_conn.execute("SELECT * FROM customertable WHERE id>(SELECT COUNT(*) FROM customertable) - 15")
    i=10 
    Label(root,text="ID",fg='#061f12',background="#c49080",width=21).grid(row=9,column=0)
    Label(root,text="NAME",fg='#061f12',background="#c49080",width=21).grid(row=9,column=1)
    Label(root,text="PHONE",fg='#061f12',background="#c49080",width=21).grid(row=9,column=2)
    Label(root,text="MAIL",fg='#061f12',background="#c49080",width=21).grid(row=9,column=3)
    Label(root,text="DATE",fg='#061f12',background="#c49080",width=21).grid(row=9,column=4)
    for data in my_conn: 
        for j in range(len(data)):
            e = Entry(root, width=25, fg='#061f12',background="#c49080",borderwidth=1, relief="solid") 
            e.grid(row=i, column=j) 
            e.insert(END, data[j])
        i=i+1

#window

root = Tk()
root.title("TAYLORMASTER")
root.geometry("770x600")
root.iconbitmap("measuring.ico")
root.configure(background="#f3d6cd")
global e1
global e2
global e3
global e4

v=IntVar(root)
v.set(2)

show()



#font

my_font = Font(
    family = 'Times',
    size = 12,
    weight = 'bold',
    slant = 'roman',
    underline = 0,
    overstrike = 0
)

#labels

Label(root,text="ENTER THE CUSTOMER DETAILS",fg="#223e02",height=2,background="#f3d6cd",font=my_font).place(x=180,y=310)
Label(root,text="Customer Id :",fg="#800709",background="#f3d6cd").place(x=10,y=350) 
Label(root, text="Name :",fg="#800709",background="#f3d6cd").place(x=240, y=350)
Label(root, text="Phone no :",fg="#800709",background="#f3d6cd").place(x=440, y=350)
Label(root, text="mail :",fg="#800709",background="#f3d6cd").place(x=10, y=390)
Label(root, text="Gender :",fg="#800709",background="#f3d6cd").place(x=260, y=390)
 
#textfields

e1 = Entry(root,fg="#800709")
e1.place(x=100, y=350)
 
e2 = Entry(root,fg="#800709")
e2.place(x=300, y=350)
 
e3 = Entry(root,fg="#800709")
e3.place(x=520, y=350)

e4 = Entry(root,fg="#800709",width=30)
e4.place(x=60,y=390)
 
#radiobutton

rb1=Radiobutton(root,text="male",variable=v,value=1,background="#f3d6cd",command=rb).place(x=315,y=390)
rb2=Radiobutton(root,text="female",variable=v,value=2,background="#f3d6cd",command=rb).place(x=370,y=390)

#button

Button(root, text="Submit", command=Ok,fg="#223e02",width=10,background="#c49080",borderwidth=0).place(x=270, y=450)


root.mainloop()