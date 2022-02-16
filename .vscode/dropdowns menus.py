#=============================================================================================
import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()

#============================================================================================

'''import tkinter
from tkinter import*

root =  Tk()
root.title('Dropdown Menus')
root.geometry('400x400')

def show():
    MyLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop =  OptionMenu(root, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
drop.pack()

myButton = Button(root,clicked, text="show Selection", command=show)
myButton.pack()

root.mainloop()'''