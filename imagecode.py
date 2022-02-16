from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("IMAGE")

my_img = ImageTk.PhotoImage(Image.open("123.png"))
my_label = Label(image = my_img)
my_label.pack()

root.mainloop()
