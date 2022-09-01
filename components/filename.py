import os
from tkinter import *

root = Tk()
file_path = root.filename

def open():
    global my_image
    root.filename =filedialog.askopenfilename(initialdir="/images", title="Select a file", filetypes=(("jpeg files", "*.jpg"),("png files", "*.png"),("All files", "*.*")))
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(root, image=my_image).pack()

def listDir(dir):
    fileNames = os.listdir(dir)
    for fileName in fileNames:
        print('File Name: ' + fileName)

uploadbtn = Button(text="Upload Images", command=open).pack()
        

root.mainloop()