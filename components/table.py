from tkinter import *
import os
import tkinter as ttk
from subprocess import Popen
from PIL import ImageTk, Image
from tkinter import filedialog
import datetime
import sys
import time


window = Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
i=2
rows = []
current_id = 0
label_ids = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

def exit():
    window.destroy()

canvas = Canvas(window, height = 1000, width = 1500, bg='#363534')
canvas.pack()

frame = Frame(window, bg = '#5A5A5A')
frame.place(relwidth = 0.9, relheight = 0.7, relx = 0.05, rely = 0.2)
exitbtn = Button(window, text="Exit", command = exit).place(relwidth = 0.15, relheight = 0.08, relx = 0.8, rely = 0.05)

table = Canvas(frame, bg = '#C4C4C4')
table.place(relwidth = 0.6, relheight = 0.9, relx = 0.02, rely = 0.05)

v0 = StringVar()
e0 = Entry(table, textvariable = v0, state = 'readonly')
v0.set('Present')
e0.grid(row = 1, column = 0 )

v1 = StringVar()
e1 = Entry(table, textvariable = v1, state = 'readonly')
v1.set('Name')
e1.grid(row = 1, column = 1 )

v2 = StringVar()
e2 = Entry(table, textvariable = v2, state = 'readonly')
v2.set('Entry Time')
e2.grid(row = 1, column = 2)

v3 = StringVar()
e3 = Entry(table, textvariable = v3, state = 'readonly')
v3.set('Reason for Absence')
e3.grid(row = 1, column = 3 )


for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            student = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            if not student in label_ids:
                label_ids[student] = current_id 
                current_id += 1
                id_ = label_ids[student]
                print(id_)

#current_id = total no folder
#y = numbers
#students = just names
#label_ids = names and numbers
#id_ = 
# for x in label_ids:
#     y = label_ids[x]
#     print(y)


for student in os.listdir('./images'):
    i=i+1
    items = []
    var = IntVar()
    c = Checkbutton(table, variable = var, bg = "#C4C4C4")
    c.val = var
    items.append(c)
    c.grid(row = i, column = 0)
    
    for j in range(1,4):
        if j == 1:
            b = Label(table, text=student, width=20, bg = "#ffffff")

        elif j == 2:
            b = Entry(table, width=25, bg = "#ffffff")
            


        else:
            b = Entry(table, width=25, bg = "#ffffff")

        items.append(b)
        b.grid(row=i, column=j)
    rows.append(items)


window.mainloop()