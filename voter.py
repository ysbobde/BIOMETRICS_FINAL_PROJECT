import tkinter as tk
import socket
from tkinter import *
from VotingPage import votingPg
from PIL import ImageTk,Image


def establish_connection():
    host = socket.gethostname()
    port = 4001
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(client_socket)
    message = client_socket.recv(1024)      #connection establishment message   #1
    if(message.decode()=="Connection Established"):
        return client_socket
    else:
        return 'Failed'


def failed_return(frame1,client_socket,message):
    for widget in frame1.winfo_children():
        widget.destroy()
    message = message + "... \nTry again..."
    Label(frame1, text=message, font=('Helvetica', 12, 'bold')).grid(row = 1, column = 1)
    client_socket.close()

def log_server(root,frame1,client_socket,voter_ID,password):
    message = voter_ID + " " + password
    client_socket.send(message.encode()) #2
    print(message)
    message = client_socket.recv(1024) #Authenticatication message
    message = message.decode()
    print(message)
    if(message=="Authenticate"):
        votingPg(root, frame1, client_socket)

    elif(message=="VoteCasted"):
        message = "Vote has Already been Cast"
        failed_return(frame1,client_socket,message)

    elif(message=="InvalidVoter"):
        message = "Invalid Voter"
        failed_return(frame1,client_socket,message)

    else:
        message = "Server Error"
        failed_return(frame1,client_socket,message)



def voterLogin(root,frame1):

    client_socket = establish_connection()
    if(client_socket == 'Failed'):
        message = "Connection failed"
        failed_return(root,frame1,client_socket,message)

    root.title("Voter Login")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Voter Login", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 2, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)
    Label(frame1, text="Voter ID:      ", anchor="e", justify=LEFT).grid(row = 2,column = 0)
    voter_ID = tk.StringVar()
    e1 = Entry(frame1, textvariable = voter_ID)
    e1.grid(row = 3,column = 2)
    Radiobutton(frame1, text = "1", indicator = 0, height = 4, width=15,command = lambda: log_server(root, frame1, client_socket, voter_ID.get(),"101_1.tif")).grid(row = 4,column = 0)
    finger1 = ImageTk.PhotoImage((Image.open("database/101_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing1= Label(frame1, image=finger1).grid(row = 4,column = 0)


    Radiobutton(frame1, text = "1", indicator = 0, height = 4, width=15,command = lambda: log_server(root, frame1, client_socket, voter_ID.get(),"102_1.tif")).grid(row = 4,column = 1)
    finger2 = ImageTk.PhotoImage((Image.open("database/102_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing2= Label(frame1, image=finger2).grid(row = 4,column = 1)
    
    Radiobutton(frame1, text = "1", indicator = 0, height = 4, width=15,command = lambda: log_server(root, frame1, client_socket, voter_ID.get(),"103_1.tif")).grid(row = 4,column = 2)
    finger3 = ImageTk.PhotoImage((Image.open("database/103_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing3= Label(frame1, image=finger3).grid(row = 4,column = 2)
    
    Radiobutton(frame1, text = "1", indicator = 0, height = 4, width=15,command = lambda: log_server(root, frame1, client_socket, voter_ID.get(),"104_1.tif")).grid(row = 4,column = 3)
    finger4= ImageTk.PhotoImage((Image.open("database/104_1.tif")).resize((60,60),Image.ANTIALIAS))
    fing4= Label(frame1, image=finger4).grid(row = 4,column = 3)
    

    frame1.pack()
    root.mainloop()


if __name__ == "__main__":
        root = Tk()
        root.geometry('500x500')
        frame1 = Frame(root)
        voterLogin(root,frame1)