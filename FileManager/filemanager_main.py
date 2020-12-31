from tkinter import *
from filemanager_utilities import *
from PIL import ImageTk,Image
import os

root = Tk()
# creating a canvas to insert image
canv = Canvas(root, width=500, height=420, bg='white')
canv.grid(row=0, column=2)
BASE_DIR = os.path.dirname(__file__)
imagepath =os.path.join(BASE_DIR,"tkintergrid.jpg")
img = ImageTk.PhotoImage(Image.open(imagepath))  
canv.create_image(20, 20, anchor=NW, image=img)

# creating label and buttons to perform operations
Label(root, text="Arnold\'s File Manager", font=("Helvetica", 16), fg="blue").grid(row = 5, column = 2)

Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)

Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)

Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)

Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)

Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)

Button(root, text = "Make a Folder", command = create_folder).grid(row = 75, column = 2)

Button(root, text = "Remove a Folder", command = delete_folder).grid(row = 65, column =2)

Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)

root.mainloop()