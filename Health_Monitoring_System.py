import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import socket
# import TkTreectrl as tree
# from TkTreectrl import MultiListbox

from tkinter import ttk
#https://pythonprogramming.net/converting-tkinter-to-exe-with-cx-freeze/
#https://pythonbasics.org/tkinter-image/
#OOOWeb Host connection
import requests
from bs4 import BeautifulSoup
import json
#GUI
import time
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
# from tkinter import Tk, Frame, Menu
global IPaddress
IPaddress=socket.gethostbyname(socket.gethostname())

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, width=300, height=300)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne,PageTwo,SignUp):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def Signup(self):
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            messagebox.showinfo("No internet connection", "Please check you connection")
        else:
            if ((Name.get() !=  "") or (Password.get() != "") or (SubID.get() != "") or (Num.get() != "" )):
                print("name",Name.get())
                print(Password.get())
                print(SubID.get())
                print(Num.get())
                req=****************Enter your signup API here**************************
                r=requests.get(req)
                myhtml1=r.text
                print(myhtml1)
                if (myhtml1 == "User already exist"):
                    print("inside")
                    messagebox.showinfo("Error", "Subject Id : {Id} already exist".format(Id=SubID.get()))
                    Name.delete(0, END)
                    Password.delete(0, END)
                    SubID.delete(0, END)
                    Num.delete(0, END)
                elif (myhtml1 == "successful"):
                    messagebox.showinfo("Sign Up Successful","Click on Log In")
                    Name.delete(0, END)
                    Password.delete(0, END)
                    SubID.delete(0, END)
                    Num.delete(0, END)
                elif (myhtml1 == "Insert Fail"):
                    messagebox.showinfo("Sign Up Failed","Please Fill Valid Data ")
                    Name.delete(0, END)
                    Password.delete(0, END)
                    SubID.delete(0, END)
                    Num.delete(0, END)

            else:
                messagebox.showinfo("Invalid data", "Please Enter Valid Data")




    def logIn(self):
   
        print(UserName.get())
        print(password.get())
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            messagebox.showinfo("No internet connection", "Please check you connection")
        else:
            if (UserName.get() != "" or password.get() != ""):
                req=**************Enter your Login API here******************************
                r=requests.get(req)
                myhtml=r.text
                print(myhtml)
                # myhtml=json.loads(myhtml)
                UserName.delete(0, END)
                password.delete(0, END) 
                a = []
                if (myhtml=="Login failed. Invalid username or password"):
                    check=messagebox.showerror("error","Wrong Credentionals")
                    if check=='ok':
                        UserName.delete(0, END)
                        password.delete(0, END)
                        self.show_frame("PageOne")
                else:
                    self.show_frame("PageTwo")
                    #print("success")
            else:
                messagebox.showinfo("Invalid data", "Please Enter Valid Data")





class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # self.pack(fill=BOTH, expand=1)

        load = Image.open("blue.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        label = tk.Label(self, text="Welcome to Health Monitoring", font=controller.title_font)
        label.pack(side="top", fill="x", pady=5)
        label = tk.Label(self, text="Powered by 0550Projects", font=controller.title_font)
        label.pack(side="bottom", fill="x", pady=5)
        button1 = tk.Button(self, text="Log In",height = 2,width = 5, command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Sign Up",height = 2,width = 5, command=lambda: controller.show_frame("SignUp"))
        button3 = tk.Button(self, text="Exit",height = 2,width = 5, command=self.quit)
        button1.pack()
        button2.pack()
        button3.pack()

        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller

        load = Image.open("blue.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        global UserName,password
        label = tk.Label(self, text="Welcome to health Monitoring", font=controller.title_font)
        label.pack(side="top", fill="x", pady=5)
        label = tk.Label(self, text="Powered by 0550Projects", font=controller.title_font)
        label.pack(side="bottom", fill="x", pady=5)
        name_label=Label(self,text="User Name",background="white")
        name_label.pack(pady=5)
        UserName =Entry(self,width=30)
        UserName.pack(pady=5)
        Password_label=Label(self,text="Password",background="white")
        Password_label.pack(pady=5)
        password =Entry(self,show="*",width=30)
        password.pack(pady=5)
        LogIn=Button(self,text='Log In',height = 2,width = 5,command=controller.logIn)
        LogIn.pack(pady=5)
        button = tk.Button(self, text="Back",height = 2, width = 5,command=lambda: controller.show_frame("StartPage"))
        button.pack(pady=5)
        SignUp = tk.Button(self, text="Sign Up",height = 2, width = 5,command=lambda: controller.show_frame("SignUp"))
        SignUp.pack(pady=5)

class PageTwo(tk.Frame):

    # tk5=Entry(self, font = ("Times New Roman", 10))
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        load = Image.open("blue.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        for label in self.grid_slaves():
            if int(label.grid_info()["row"]):
                label.grid_forget()        


        ttk.Label(self, text = "Subject ID :", 
                font = ("Times New Roman", 10)).grid( 
                 padx = 10, pady = 25,row=2,column=0) 
        
        # Combobox creation 
        n = tk.StringVar() 
        global subjectID,myhtml1
        global value
        value=""
        subjectID = ttk.Combobox(self, width = 27, textvariable = n) 
        

        req="https://0550softwares.000webhostapp.com/hemophiliaApi/post_subids.php"
        r=requests.get(req)
        myhtml=r.text
        myhtml=myhtml.strip()
        # print(myhtml)
        array=myhtml.split(' ')
        array=tuple(array)
        # Adding combobox drop down list 
        subjectID['values'] = array
        subjectID.grid(row = 2,column=1) 
        subjectID.current()
        global tk1,tk2,tk3,tk4,tk5
        self.tk1=Entry(self, font = ("Times New Roman", 10))
        self.tk2=Entry(self, font = ("Times New Roman", 10))
        self.tk3=Entry(self, font = ("Times New Roman", 10))
        self.tk4=Entry(self, font = ("Times New Roman", 10))
        self.tk5=Entry(self, font = ("Times New Roman", 10))
        self.LabelPass = Label(self, text="Password",font = ("Times New Roman", 10,'bold'))
        self.LabelPass.grid(row=2,column=5,padx = 10, pady = 25)
        self.EntryPass=Entry(self, font = ("Times New Roman", 10))
        self.EntryPass.grid(padx = 10, pady = 25,row=2,column=6)


        self.tk1.delete(0, 'end')
        self.tk2.delete(0, 'end')
        self.tk3.delete(0, 'end')
        self.tk4.delete(0, 'end')
        self.tk5.delete(0, 'end')

        self.tk1.destroy()
        self.tk2.destroy()
        self.tk3.destroy()
        self.tk4.destroy()
        self.tk5.destroy()
        
        Search = tk.Button(self, text="Search",font = ("Times New Roman", 10),command=self.searchBySubID)
        Search.grid(row=2,column=2,padx = 10, pady = 25,)

        Logout = tk.Button(self, text="Log Out",font = ("Times New Roman", 10),command=lambda: controller.show_frame("StartPage"))
        Logout.grid(row=2,column=15,padx = 10, pady = 25,)
        
        
# data
    def searchBySubID(self):
        IPaddress=socket.gethostbyname(socket.gethostname())
        if IPaddress=="127.0.0.1":
            messagebox.showinfo("No internet connection", "Please check you connection")
        else:
            # Logout = tk.Button(self, text="Log Out",font = ("Times New Roman", 10),command=lambda: controller.show_frame("StartPage"))
            # Logout.grid(row=2,column=20,padx = 10, pady = 25,)

            # for Entry in self.grid_slaves():
            #     if int(Entry.grid_info()["row"]):
            #         Entry.grid_forget()   
            for i in range(2):
                self.tk1.destroy()
                self.tk2.destroy()
                self.tk3.destroy()
                self.tk4.destroy()
                self.tk5.destroy()
                self.LabelPass.destroy()
                self.EntryPass.destroy()
            
            global value
            value=subjectID.get()
            #Get password
            req=*************Enter the API to fetch data using subjectID********************************
            passw=requests.get(req)
            myhtmlPass=passw.text

            self.LabelPass = Label(self, text="Password",font = ("Times New Roman", 10,"bold"))
            self.LabelPass.grid(row=2,column=5,padx = 10, pady = 25)
            self.EntryPass=Entry(self, font = ("Times New Roman", 10))
            self.EntryPass.grid(padx = 10, pady = 25,row=2,column=6) 
            self.EntryPass.insert(END,myhtmlPass)


            print(value)
            req1=**************API*************************************************************
            r1=requests.get(req1)
            myhtml1=r1.text
            myhtml1=json.loads(myhtml1)
            
            print(len(myhtml1[0]))
            # print(len(myhtml1[0][0]))
            print(myhtml1[0][0]['PatientName'])



            Patient_Name=Label(self, text = "Patient Name", font = ("Times New Roman",16,'bold')).grid(padx = 10, pady = 25,row=5,column=0)         
            Subject_ID=Label(self, text = "Subject ID",font = ("Times New Roman", 16,'bold')).grid(padx = 10, pady = 25,row=5,column=1) 
            Dose_Time=Label(self, text = "Dose Time",font = ("Times New Roman", 16,'bold')).grid(padx = 10, pady = 25,row=5,column=2) 
            Bleed_Location=Label(self, text = "Bleed Location",font = ("Times New Roman", 16,'bold')).grid(padx = 10, pady = 25,row=5,column=3) 
            Last_updated=Label(self, text = "Last updated",font = ("Times New Roman", 16,'bold')).grid(padx = 10, pady = 25,row=5,column=4) 

            count=len(myhtml1[0])
       
            row=6
            for i in range(0,count):
                self.tk1=Entry(self, font = ("Times New Roman", 10))
                self.tk1.grid(padx = 10, pady = 25,row=row,column=0) 
                self.tk1.insert(END,myhtml1[0][i]['PatientName'])
                self.tk2=Entry(self, font = ("Times New Roman", 10))
                self.tk2.grid(padx = 10, pady = 25,row=row,column=1) 
                self.tk2.insert(END,myhtml1[0][i]['user_subject_id'])
                self.tk3=Entry(self, font = ("Times New Roman", 10))
                self.tk3.grid(padx = 10, pady = 25,row=row,column=2)
                self.tk3.insert(END,myhtml1[0][i]['DoseTime']) 
                self.tk4=Entry(self, font = ("Times New Roman", 10))
                self.tk4.grid(padx = 10, pady = 25,row=row,column=3) 
                self.tk4.insert(END,myhtml1[0][i]['BleedLocation'])
                self.tk5=Entry(self, font = ("Times New Roman", 10))
                self.tk5.grid(padx = 10, pady = 25,row=row,column=4)
                self.tk5.insert(END,myhtml1[0][i]['LogDateTime'])             
                row= row+1
            
            # scrollbar = Scrollbar(self)
            # scrollbar.pack(side=RIGHT, fill=Y)
            
            # scrollbar.config()
            # Logout = tk.Button(self, text="Log Out",font = ("Times New Roman", 10),command=lambda: controller.show_frame("StartPage"))
            # Logout.grid(row=2,column=20,padx = 10, pady = 25,)


class SignUp(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller

        load = Image.open("blue.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        global Name,Password,SubID,Num

        UserName=Label(self, text="User Name",width=13,font = ("Times New Roman",12,'bold'))
        UserName.grid(row=1,column=0)

        Name=Entry(self, font = ("Times New Roman", 10))
        Name.grid(padx = 10, pady = 25,row=1,column=1) 
        
        
        UserPassword=Label(self, text="Password",width=13,font = ("Times New Roman",12,'bold'))
        UserPassword.grid(row=2,column=0)
        
        Password=Entry(self, font = ("Times New Roman", 10))
        Password.grid(padx = 10, pady = 25,row=2,column=1) 


        UserSubjectId=Label(self, text="Subject Id",width=13,font = ("Times New Roman",12,'bold'))
        UserSubjectId.grid(row=3,column=0)
        
        SubID=Entry(self, font = ("Times New Roman", 10))
        SubID.grid(padx = 10, pady = 25,row=3,column=1) 
        
        UserPhoneNum=Label(self, text="Mobile Number",width=13,font = ("Times New Roman",12,'bold'))
        UserPhoneNum.grid(row=4,column=0)

        Num=Entry(self, font = ("Times New Roman", 10))
        Num.grid(padx = 10, pady = 25,row=4,column=1)

        Sign = tk.Button(self, text="Sign Up",font = ("Times New Roman",12,'bold'),command=controller.Signup)
        Sign.grid(row=5,column=1,padx = 10, pady = 10,)
        Log = tk.Button(self, text="Log In",font = ("Times New Roman",12,'bold'),command=lambda: controller.show_frame("PageOne"))
        Log.grid(row=6,column=1,padx = 10, pady = 25,)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_rowconfigure(3, weight=1)
        # self.grid_columnconfigure(0, weight=2)
        # self.grid_columnconfigure(6, weight=2) 





if __name__ == "__main__":


    print(IPaddress)
    if IPaddress=="127.0.0.1":
        messagebox.showinfo("No internet connection", "Please check you connection")
    else:

        global app,menubar
        SearchResult=""
        flag=0
        app = SampleApp()
        app.title("Health Monitoring System")
        app.iconbitmap("DNA.ico")
        app.minsize(1151, 544)
        # app.maxsize(1024,1024)
        menubar = Menu(app)
        # menubar.add_command(label="Hello!", command=hello)
        menubar.add_command(label="Quit!", command=app.quit)

        # display the menu
        app.config(menu=menubar)


        app.mainloop()


