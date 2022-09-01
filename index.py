from tkinter import *
import os
import tkinter as ttk
from subprocess import Popen
from PIL import ImageTk, Image
from tkinter import filedialog
import datetime
import sys
import time
from face import *

window = Tk()
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
i=0
rows = []
current_id = 0
label_ids = {}
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

class Clock(ttk.Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        ttk.Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S %p')
        else:
            self.time     = time.strftime('%H:%M:%S %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S %p')
        else:
            new_time = time.strftime('%H:%M:%S %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)

def facerecognition():
    os.system('python face.py')

def exit():
    window.destroy()

def facetrain():
    os.system('face_train.py')

def open():
    global my_image
    window.filename =filedialog.askopenfilename(initialdir="/images", title="Select a file", filetypes=(("jpeg files", "*.jpg"),("png files", "*.png"),("All files", "*.*")))
    my_image = ImageTk.PhotoImage(Image.open(window.filename))
    my_image_label = Label(listbox, image=my_image).pack()

def add_row():
    global i 
    i=i+1
    items = []
    var = IntVar()
    c = Checkbutton(table, variable = var)
    c.val = var
    items.append(c)
    c.grid(row = i+1, column = 5)
    for j in range(1,4): #Columns
        b = Entry(table)
        items.append(b)
        b.grid(row=i+1, column=j)
    rows.append(items)

def delete_row():
    for rowno, row in reversed(list(enumerate(rows))):
        if row[0].val.get() == 1:
            for i in row:
                i.destroy()
            rows.pop(rowno)


canvas = Canvas(window, height = 1000, width = 1500, bg='#363534')
canvas.pack()

frame = Frame(window, bg = '#5A5A5A')
frame.place(relwidth = 0.9, relheight = 0.7, relx = 0.05, rely = 0.2)

startbtn = Button(window, text="Start", command = facerecognition).place(relwidth = 0.2, relheight = 0.1, relx = 0.05, rely = 0.05)
exitbtn = Button(window, text="Exit", command = exit).place(relwidth = 0.15, relheight = 0.08, relx = 0.8, rely = 0.05)
var = ("To exit out of Face recognition press 'ESC'")
exitfacelabel = Label(window, text = "To exit out of Facial Recognition press 'ESC'").place(relx = 0.058, rely = 0.15)
trainbtn = Button(frame, text="Face Train", command=facetrain).place(relwidth = 0.1, relheight = 0.05, relx = 0.67, rely = 0.83)

uploadbtn = Button(frame, text="Upload Images", command=open)
uploadbtn.place(relwidth = 0.1, relheight = 0.05, relx = 0.85, rely = 0.03)

listbox = Listbox(frame)
listbox.place(relwidth = 0.3, relheight = 0.7, relx = 0.65, rely = 0.1)

clock1 = Clock(frame)
clock1.place(relwidth = 0.1, relheight = 0.05, relx = 0.65, rely = 0.03)
# date = Label(frame, text=f"{datetime.datetime.now():%a, %b %d %Y}").place(relwidth = 0.1, relheight = 0.05, relx = 0.74, rely = 0.03)

table = Canvas(frame)
table.place(relwidth = 0.6, relheight = 0.9, relx = 0.02, rely = 0.05)

bt = ttk.Button(table , text = 'Add Row', command = add_row)
bt.grid(row =0, column=2)

dl = ttk.Button(table , text = 'Delete Row', command = delete_row)
dl.grid(row =0, column=3)


v0 = StringVar()
e0 = Entry(table, textvariable = v0, state = 'readonly')
v0.set("Picture")
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

v4 = StringVar()
e4 = Entry(table, textvariable = v4, state = 'readonly')
v4.set('Present/Absent')
e4.grid(row = 1, column = 5 )





for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            student = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            if not student in label_ids:
                label_ids[student] = current_id 
                current_id += 1

# p=2
# if p==1:
#     var = IntVar(value=0)
# else:
#     var = IntVar(value=1)

# for student in os.listdir('./images'):
#     i=i+1
#     items = []
#     var = IntVar()
#     c = Checkbutton(table, variable = var)
#     c.val = var
#     items.append(c)
#     c.grid(row = i+1, column = 0)


for index, x in enumerate(label_ids):
    num = 1 # x-axis
    index += 2 #y-axis
    person = Label(table, text = x)
    person.grid(row=index,column=num)
    # print(id_)
    # print(x)
    # print(name)
    i = i + 1
    try:
        if x == name:
            var = IntVar(value=1)
        else:
            var = IntVar(value=0)
        c = Checkbutton(table, variable = var)
        c.val = var
        c.grid(row = i+1, column = 5)
    except NameError:
        print("ERROR NOONE FOUND")
    
try:
    if id_ == 0:
        time_row = 2
        print(time_row)
        # print(id_)
    else:
        time_row = id_ + 2
        print(time_row)
        print(id_)


    person1 = Label(table, text=time_arrive)
    person1.grid(row=time_row, column=num+1)
    person2 = Label(table, text=time_arrive)
    person2.grid(row=time_row, column=num+1)
    person3 = Label(table, text=time_arrive)
    person3.grid(row=time_row, column=num+1)
    person4 = Label(table, text=time_arrive)
    person4.grid(row=time_row, column=num+1)
    person5 = Label(table, text=time_arrive)
    person5.grid(row=time_row, column=num+1)
except NameError:
    print("Not Found")



window.mainloop()