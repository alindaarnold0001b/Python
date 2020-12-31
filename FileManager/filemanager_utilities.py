from tkinter import *
import shutil         
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# open a file box window 
# Especially when we want to select a file
def open_window():
    read=easygui.fileopenbox()
    return read


# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")


# copying file function
def copy_file():
    sourcefilepath = open_window()
    destinationfilepath=filedialog.askdirectory()
    shutil.copy(sourcefilepath,destinationfilepath)
    mb.showinfo('confirmation', "File successfully Copied !")


# deleting file function
def delete_file():
    file_to_delete_loc = open_window()
    if os.path.exists(file_to_delete_loc):
        os.remove(file_to_delete_loc)    
        mb.showinfo('confirmation', "Successfully Deleted !")         
    else:
        mb.showinfo('confirmation', "File not found !")




# renaming file function
def rename_file():
    chosenFilepath = open_window()
    chosenfile_dir = os.path.dirname(chosenFilepath)
    extension=os.path.splitext(chosenfile_dir)[1]
    print("Enter new name for the chosen file")
    new_name=input()
    path = os.path.join(chosenfile_dir, new_name+extension)
    print(path)
    try:
        os.rename(chosenFilepath,path)
        mb.showinfo('confirmation', "File Renamed Successfully !")
    except:
        mb.showinfo("confirmation","Oops Something went wrong!!")
    

# moving a file function
def move_file():

    source = open_window()
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        try:
            shutil.move(source, destination)  
            mb.showinfo('confirmation', "File Moved successfully!")
        except:
            mb.showinfo("comfirmation","Destination path already exists!")

# function to create a new folder
def create_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")

    newFolderName=input()
    path = os.path.join(newFolderPath, newFolderName)  

    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")


# function to remove a folder
def delete_folder():
    delFolder_dir = filedialog.askdirectory()
    try:
        os.rmdir(delFolder_dir)
        mb.showinfo('confirmation', "Folder Deleted Successfully!")
    except:
        mb.showinfo("comfirmation","OoP Something went wrong")

# function to list all the files in folder
def list_files():
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

