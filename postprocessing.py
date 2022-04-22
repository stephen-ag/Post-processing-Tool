###------- this macro works for the files inloacation C:\Users\stephen.arput\Documents\RESULTS\LOC222\LOC2--
###-------file path customization needs to be done...in later version...
####------- Error handling has to be taken in the later version.....

from tkinter import filedialog
from PIL import ImageTk,Image
import os
from tqdm import tqdm
from tkinter import *
from tkinter import ttk
from Concatenate_files_allfolder import concat
from Main_file import loadcase
from File_collection import collect
from principal_stress_all_infolder import principal
root = Tk()
root.geometry("1600x1600+20+40")
root['bg']='lightblue'
root['bd']= 3
# image resizing


img = ImageTk.PhotoImage(file ="fatigue1.png")


panel = Label(root, image = img, height = 400, width = 300)
panel.place(x=1000, y=250)
#oldlace'azure'
root.title('Fatigue Postprocessing Tool v1.0 ')
Label(root,text = "Fatigue Postprocessing Tool v1.0 ", bg="Dodgerblue3",height ="2",\
      width = "800", fg ="white",
      font = ("Calibri",40)).pack()
Label(root,text = "Note: This tool is specific to project requirement, read the requirement\
  of this tool for process and input data. Files with binary excel format not supported",
      height ="3",
      width = "400",
      font = ("Calibri",12)).pack()
print("entering post processing module")

##---progress bar
#progbar = ttk.Progressbar(root, orient= HORIZONTAL,length= 220, mode="indeterminate")
#progbar.place(x=500, y=340)
##progbar.pack(pady =20)
#progbar.start()

e=Entry(root, width =50, font=('Arial 14'),borderwidth = 5)

e.pack(padx=10, pady=10)
e.insert(0,'Enter the path Name:')
fpath = e.get()
print("getting path from string")
print(fpath)
#fpath = 'C:\\Users\\stephen.arput\\Documents\\RESULTS\\LOC222\\LOC2'
#greet = concat(fpath)
#my_label1= Label(root, text = "" ).pack()

global frame
def clearframe():
    print("entering clear function")
        #my_label1.pack_forget()
    root.my_label1.destroy()

def submit():
    global my_label1
    global fpath
    fpath=e.get()
    greet=concat(e.get())
    frame = Frame(root, width=300, height=150,highlightbackground="blue",highlightthickness=2)
    frame.place(x=500, y=250)
    my_label1 = Label(frame, text=greet,font=("Arial", 12)).pack()
    #folderpath= "\n Entered path : "+ fpath
    #my_label1=Label(root,text=greet).pack()
    #e.delete(0, END)
    print(fpath)
    return fpath

def prbar():
    progbar = ttk.Progressbar(root, orient=HORIZONTAL, length=220, mode="indeterminate")
    progbar.place(x=500, y=340)
    progbar.start()
    #progbar.stop()

def stress():
    global fpath
    #fpath = submit()
    results=loadcase(e.get())
    frame = Frame(root, width=300, height=150,highlightbackground="blue",highlightthickness=2)
    frame.place(x=500, y=307)
    my_label1 = Label(frame, text=results,font=("Arial", 12)).pack()
    #folderpath= "\n Entered path : "+ fpath
    #my_label1=Label(root,text=results).pack()
    #e.delete(0, END)




def group():

    grouped=collect(e.get())
    frame = Frame(root, width=300, height=150,highlightbackground="blue",highlightthickness=2)
    frame.place(x=500, y=375)
    my_label1 = Label(frame, text=grouped,font=("Arial", 12)).pack()
    #folderpath= "\n Entered path : "+ fpath
    #my_label1=Label(root,text=grouped).pack()
    #e.delete(0, END)

def prin_stress():
    global my_label1

    stress_results=principal(e.get())
    frame = Frame(root, width=300, height=150,highlightbackground="blue",highlightthickness=2)
    frame.place(x=500, y=525)

    my_label1 = Label(frame, text=stress_results,font=("Arial", 12)).pack()
    #folderpath= "\n Entered path : "+ fpath
    #my_label1=Label(root,text=stress_results).pack()
    #e.delete(0, END)

#filepath = concat(fpath)



def close():
    root.destroy()

print("entering button controls")
#---------------------------------

button1 = Button(root,text = "Concatenate_AllFiles", height ="2", width = "25",\
                 font = ("Calibri",13),bg="dodgerblue3",fg ="white", command = submit)
button1.place(x = 60, y = 240)

#---------------------------------
button2 = Button(root,text = "  Compute delta Stress results",height ="2", width = "25",\
                 font = ("Calibri",13),bg="dodgerblue3",fg ="white", command =stress)
button2.place(x = 60, y = 307)
#--------------------------------

#---------------------------------
button3 = Button(root,text = "  Group files  @each path",height ="2", width = "25",\
                 font = ("Calibri",13),bg="dodgerblue3",fg ="white", command =group)
button3.place(x = 60, y = 375)
#--------------------------------
#---------------------------------
#button4= Button(root,text = " Load case combination ",height ="2", width = "25",\
#                 font = ("Calibri",13),bg="dodgerblue3",fg ="white")
#button4.place(x = 60, y = 450)
#--------------------------------
#---------------------------------
button5= Button(root,text = " Compute Principle stress ",height ="2", width = "25",\
                 font = ("Calibri",13),bg="dodgerblue3",fg ="white",command = prin_stress)
button5.place(x = 60, y = 525)
#--------------------------------
#---------------------------------
button6 = Button(root,text = " Close ",height ="2", width = "25",\
                 font = ("Calibri",13),bg="dodgerblue3",fg ="white", command = close)
button6.place(x = 60, y = 600)
#--------------------------------
print("completed button controls")
root.state("zoomed")
root.mainloop()