import tkinter 
from tkinter import *
import sqlite3
from tkinter import tkMessageBox

root=Tk()
root.title("Payments")
root.geometry("500x600")


def action():
    a = Username.get()
    b = Password.get()


conn= sqlite3.connect("cloths.db")
c = conn.cursor()
c.execute("INSERT INTO LOGIN VALUES('"+Username+"','"+Password+"')")
tkMessageBox.showinfo("Information","Your record is inserted")
conn.commit()
conn.close()


def next():
    nx=Tk()
    nx.geometry("500x650")
    nx.title("Student registration records")

    label = Label(nx, text = "Student Registration Records")
    label.grid(row=0, column=0, columnspan=20)

    p1 = Label(nx, text = "Student Registration Records")
    p1.grid(row=0, column=1, columnspan=20)

    p2 = Label(nx, text = "Student Registration Records")
    p2.grid(row=0, column=2, columnspan=20)



conn = sqlite3.connect("cloths.db")
c = conn.cursor()
c.execute("SELECT * FROM login")
r = c.fetchall()

num = 2
for i in r:
    Username = Label(root, text = i[0], font= "time 12 bold", fb ="blue")
    Username.grid(row=num, column = 0, padx=10, pady=10)

    Password = Label(root, text = i[1], font= "time 12 bold", fb ="blue")
    Password.grid(row=num, column = 1, padx=10, pady=10)


    num = num + 1

conn.commit()
conn.close()


root.mainloop()