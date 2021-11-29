import tkinter as tk
import dframe as df
import Admin as adm
from tkinter import ttk
from Admin import *
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def reg_server(root,frame1,Aad_num,name,sex,city,passw):
    
    vid = df.taking_data_voter(Aad_num,name, sex,city, passw)
    for widget in frame1.winfo_children():
        widget.destroy()
    txt = "Registered Voter with\n\n VOTER I.D. = " + str(vid)
    Label(frame1, text=txt, font=('Helvetica', 18, 'bold')).grid(row = 2, column = 1, columnspan=2)


def Register(root,frame1):

    root.title("Register Voter")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Register Voter", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Aadhar number:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    Label(frame1, text="Name:         ", anchor="e", justify=LEFT).grid(row = 3,column = 0)
    Label(frame1, text="Sex:              ", anchor="e", justify=LEFT).grid(row = 4,column = 0)
    Label(frame1, text="City:             ", anchor="e", justify=LEFT).grid(row = 6,column = 0)
    Label(frame1, text="Biometric:   ", anchor="e", justify=LEFT).grid(row = 7,column = 0)
    
   
    Aad_num = tk.StringVar()
    name = tk.StringVar()
    sex = tk.StringVar()
    city = tk.StringVar()
    fingerprint= tk.StringVar()

    e1 = Entry(frame1, textvariable = Aad_num).grid(row = 2, column = 2)
    e2 = Entry(frame1, textvariable = name).grid(row = 3, column = 2)
    e6 = Entry(frame1, textvariable = city).grid(row = 6, column = 2)
    e7 = Entry(frame1, textvariable = fingerprint).grid(row = 7, column = 2)
    
   
    e4 = ttk.Combobox(frame1, textvariable = sex, width=17)
    e4['values'] = ("Male","Female","Other")
    e4.grid(row = 4, column = 2)
    e4.current()

    e7 = ttk.Combobox(frame1, textvariable =fingerprint, width=17)
    e7['values'] = ("1","2","3","4")
    e7.grid(row = 7, column = 2)
    e7.current()
    

    Radiobutton(frame1, text = "1", variable = fingerprint, value = "101_1.tif", indicator = 0, height = 4, width=15,).grid(row = 10,column = 0)
    finger1 = ImageTk.PhotoImage((Image.open("database/101_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing1= Label(frame1, image=finger1).grid(row = 10,column = 0)

    Radiobutton(frame1, text = "2", variable = fingerprint, value = "102_1.tif", indicator = 0, height = 4, width=15,).grid(row = 10,column = 1)
    finger2 = ImageTk.PhotoImage((Image.open("database/102_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing2= Label(frame1, text="1", image=finger2).grid(row = 10,column = 1)
    
    Radiobutton(frame1, text = "1", variable = fingerprint, value = "103_1.tif", indicator = 0, height = 4, width=15,).grid(row = 10,column = 2)
    finger3 = ImageTk.PhotoImage((Image.open("database/103_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing3= Label(frame1, text="1", image=finger3).grid(row = 10,column = 2)

    Radiobutton(frame1, text = "1", variable = fingerprint, value = "104_1.tif", indicator = 0, height = 4, width=15,).grid(row = 10,column = 3)
    finger4 = ImageTk.PhotoImage((Image.open("database/104_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing4= Label(frame1, text="1", image=finger4).grid(row = 10,column = 3)

    reg = Button(frame1, text="Register", command = lambda: reg_server(root, frame1, Aad_num.get(),name.get(), sex.get(), city.get(), fingerprint.get()), width=10)
    Label(frame1, text="").grid(row = 13,column = 0)
    reg.grid(row = 14, column = 3, columnspan = 2)
    
    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         Register(root,frame1)
