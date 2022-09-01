from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root = Tk()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="/images", title="Select a file", filetypes=(("png files", "*.png"),("jpeg files", "*.jpeg")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

# my_btn = Button(root, text="Open File", command= open).pack()
def my_btn(i):
    return tk.Button(i, text="open File", command = open)

root.mainloop()