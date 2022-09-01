from tkinter import * 
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

def open():
    global my_image
    root.filename =filedialog.askopenfilename(initialdir="/images", title="Select a file", filetypes=(("jpeg files", "*.jpg"),("png files", "*.png"),("All files", "*.*")))
    # my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

btn = Button(root, text="Open File", command=open).pack()

root.mainloop()