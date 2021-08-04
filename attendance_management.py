from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import os
from tkinter import ttk
import time
import pymysql
import regex
def window4():
    global back2
    global root
    global mserial
    global mname
    global mrollno
    global myear
    global mcategory
    global mdate
    global mdepartment
    global mmonth
    global mstatus
    global msubjects
    global search_by
    global search_txt
    global add
    global update
    global clear
    global delete
    global clock
    global backoption
    root=Toplevel()
    root.title("Attendance Management System")
    root.geometry("1350x700+0+0")
    root.configure(background="black")
    root.iconbitmap("icon.ico")
    title=Label(root,text="Attendance Management System",font=("Times New Roman",40,"bold"),bg="red4",fg="white",bd=10,relief=GROOVE)
    title.pack(side=TOP,fill=X)#relwidth is used to adjust with the width ,we can also use (fill=X and side=TOP)
    clock=tk.Label(root,font=("Times New Roman",20,"bold"),bg="black",fg="white",relief=GROOVE)
    clock.place(x=11,y=11,width=200,height=60)
    tick()

        #---manage frame---
    mserial=StringVar()
    mname=StringVar()
    mrollno=StringVar()
    myear=StringVar()
    mcategory=StringVar()
    mdepartment=StringVar()
    mmonth=StringVar()
    mstatus=StringVar()
    msubjects=StringVar()
    search_by=StringVar()
    search_txt=StringVar()
    mdate=StringVar()
        
    Manage_frame=Frame(root,relief=RIDGE,bd=4,bg="red4")
    Manage_frame.place(x=20,y=95,width=450,height=610)
    m_title=Label(Manage_frame,text="Manage Students",fg="white",font=("Times New Roman",20,"bold"),bg="red4")
    m_title.grid(row=0,columnspan=2,pady=10)

        #self.button_frame=Frame(Manage_frame,relief=GROOVE,width=440,height=90,bg="red4",bd=10)
        #self.button_frame.place(x=0,y=530)

    serial=Label(Manage_frame,text="S.No",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    serial.grid(row=1,column=0,padx=20,pady=5,sticky="W")
    serial1=Entry(Manage_frame,textvariable=mserial,font=("Times New Roman",15))
    serial1.grid(row=1,column=1,padx=20,pady=5,sticky="W")
        
    name=Label(Manage_frame,text="Name",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    name.grid(row=2,column=0,padx=20,pady=5,sticky="W")
    name1=Entry(Manage_frame,textvariable=mname,font=("Times New Roman",15))
    name1.grid(row=2,column=1,padx=20,pady=5,sticky="W")

    roll_no=Label(Manage_frame,text="Roll No",bg="red4",activebackground="blue",fg="black",font=("Times New Roman",20,"bold"))
    roll_no.grid(row=3,column=0,padx=20,pady=5,sticky="W")
    roll_no1=Entry(Manage_frame,textvariable=mrollno,font=("Times New Roman",15))
    roll_no1.grid(row=3,column=1,padx=20,pady=5,sticky="W")

    year=Label(Manage_frame,text="Year",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    year.grid(row=4,column=0,padx=20,pady=5,sticky="W")
    year1=ttk.Combobox(Manage_frame,textvariable=myear,font=("Times New Roman",14),state='readonly')
    year1['values']=("First year","Second year","Third year","Fourth year")
    year1.grid(row=4,column=1,pady=5,padx=20)
    
    category=Label(Manage_frame,text="Category",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    category.grid(row=5,column=0,padx=20,pady=5,sticky="W")
    category1=ttk.Combobox(Manage_frame,textvariable=mcategory,font=("Times New Roman",14),state='readonly')
    category1['values']=("Freshers","Lateral Entry")
    category1.grid(row=5,column=1,pady=5,padx=20)

    department=Label(Manage_frame,text="Department",bg="red4",fg="black",font=("Times New Roman",20,"bold"))
    department.grid(row=6,column=0,padx=20,pady=5,sticky="W")
    department1=ttk.Combobox(Manage_frame,textvariable=mdepartment,font=("Times New Roman",14),state='readonly')
    department1['values']=("Computer Science and Engineering","Mechananical Engineering","Civil Engineering","Electrical Engineering","Electronics")
    department1.grid(row=6,column=1,pady=5,padx=20)

    date=Label(Manage_frame,text="Date",bg="red4",activebackground="blue",fg="black",font=("Times New Roman",20,"bold"))
    date.grid(row=7,column=0,padx=20,pady=5,sticky="W")
    date1=Entry(Manage_frame,textvariable=mdate,font=("Times New Roman",15))
    date1.grid(row=7,column=1,padx=20,pady=5,sticky="W")

    status=Label(Manage_frame,text="Status",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    status.grid(row=8,column=0,padx=20,pady=5,sticky="W")
    status1=ttk.Combobox(Manage_frame,textvariable=mstatus,font=("Times New Roman",14),state='readonly')
    status1['values']=("Present","Absent","Other Reason")
    status1.grid(row=8,column=1,pady=5,padx=20)

    month=Label(Manage_frame,text="Month",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    month.grid(row=9,column=0,padx=20,pady=5,sticky="W")
    month1=ttk.Combobox(Manage_frame,textvariable=mmonth,font=("Times New Roman",14),state='readonly')
    month1['values']=("January","February","March","April","May","June","July","August","September","October","November","December")
    month1.grid(row=9,column=1,pady=5,padx=20)

    subject=Label(Manage_frame,text="Subjects",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    subject.grid(row=10,column=0,padx=20,pady=5,sticky="W")
    subject1=ttk.Combobox(Manage_frame,textvariable=msubjects,width=22,font=("Times New Roman",14),state='readonly')
    subject1['values']=("Software Engineering","Mathemataics-3","Computer Architecture and Organization","Database Management System","Formal Language and Automata")
    subject1.grid(row=10,column=1,pady=5,padx=20)

        #----button frame---
    button_frame=Frame(Manage_frame,relief=GROOVE,bd=4,bg="red4")
    button_frame.place(x=15,y=540,width=420)

    add=Button(button_frame,text="ADD",width=10,command=add_students).grid(row=0,column=0,padx=10,pady=10)
        
    update=Button(button_frame,text="UPDATE",width=10,command=update_data).grid(row=0,column=1,padx=10,pady=10)
        
    clear=Button(button_frame,text="CLEAR",width=10,command=clear_all).grid(row=0,column=2,padx=10,pady=10)

    delete=Button(button_frame,text="DELETE",width=10,command=delete_data).grid(row=0,column=3,padx=10,pady=10)
        
        #---details frame---
    Details_frame=Frame(root,relief=RIDGE,bd=4,bg="red4")
    Details_frame.place(x=500,y=95,width=800,height=610)

    search=Label(Details_frame,text="Search",fg="black",bg="red4",font=("Times New Roman",20,"bold"))
    search.grid(row=0,column=0,padx=20,pady=10,sticky="W")
        
    search1=ttk.Combobox(Details_frame,textvariable=search_by,width=10,font=("Times New Roman",13),state='readonly')
    search1['values']=("name","month","roll_no","category","status","serial_no")#values are written here as they are written in the database
    search1.grid(row=0,column=1,pady=10,padx=20,sticky="W")
    txt_search=Entry(Details_frame,textvariable=search_txt,font=("Times New Roman",10,"bold"),bd=5,relief=GROOVE)
    txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="W")
    searchbtn=Button(Details_frame,text="Search",command=search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
    showallbtn=Button(Details_frame,text="Show All",command=fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)
    backoption=Button(Details_frame,text="back",width=10,bd=0,command=back2).grid(row=0,column=5,padx=10,pady=10)
    global Student_table
       #---table frame-----
    Table_Frame=Frame(Details_frame,relief=RIDGE,bd=4,bg="red4")
    Table_Frame.place(x=10,y=70,width=760,height=500)

    scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
    scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        #treeview allows you to make grid 
    Student_table=ttk.Treeview(Table_Frame,columns=("serial_no","name","roll_no","year","category","department","date","status","month","subjects"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command=Student_table.xview) #to set the scrolls on both the views
    scroll_y.config(command=Student_table.yview)
        #name of my table is Student_table
    Student_table.heading("serial_no",text="S.No")
    Student_table.heading("name",text="Name")
    Student_table.heading("roll_no",text="Roll No")
    Student_table.heading("year",text="Year")
    Student_table.heading("category",text="Category")
    Student_table.heading("department",text="Department")
    Student_table.heading("date",text="Date")
    Student_table.heading("status",text="Status")
    Student_table.heading("month",text="Month")
    Student_table.heading("subjects",text="Subjects")
    Student_table['show']='headings'
        #these are the widths of he columns
    Student_table.column("serial_no",width=100)
    Student_table.column("name",width=150)
    Student_table.column("roll_no",width=150)
    Student_table.column("year",width=150)
    Student_table.column("category",width=150)
    Student_table.column("department",width=150)
    Student_table.column("date",width=100)
    Student_table.column("status",width=100)
    Student_table.column("month",width=125)
    Student_table.column("subjects",width=150)
    Student_table.pack(fill=BOTH,expand=1)
    Student_table.bind("<ButtonRelease-1>",get_cursor)
    fetch_data()
        #--adding functionalities--
        #name of my database is second year and table name is student
def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%y")
    clock.config(text='Date: '+date_string+"\n"+"Time: "+time_string)
    clock.after(200,tick)
def add_students():
    if(mserial.get()=="" or mname.get()=="" or mrollno.get()=="" or myear.get()=="" or mcategory.get()=="" or mdepartment.get()=="" or mdate.get()=="" or  mstatus.get()=="" or msubjects.get()==""):
         master.withdraw()
         messagebox.showwarning("Warning","All fields are required to progress further")
    else:
        con=pymysql.connect(host="localhost",user="root",password="",database="secondyear")
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(mserial.get(),
                                                                               mname.get(),
                                                                               mrollno.get(),
                                                                               myear.get(),
                                                                               mcategory.get(),
                                                                               mdepartment.get(),
                                                                               mdate.get(),
                                                                               mstatus.get(),
                                                                               mmonth.get(),
                                                                               msubjects.get()
                                                                                     ))

        con.commit()
        fetch_data()
        clear_all()
        con.close()
        master.withdraw()
        messagebox.showinfo("Information","Your record is inserted")
def fetch_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="secondyear")
    cur=con.cursor()
          #fetchall() fetches all the rows of a query result. It returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch. cursor
    cur.execute("select*from students")
    rows=cur.fetchall()
    if(len(rows)!=0):
         Student_table.delete(*Student_table.get_children())
         for row in rows:
             Student_table.insert('',END,values=row)
             con.commit()
    con.close()
def clear_all():
    mserial.set("")
    mname.set("")
    mrollno.set("")
    myear.set("")
    mcategory.set("")
    mdepartment.set("")
    mdate.set("")
    mstatus.set("")
    mmonth.set("")
    msubjects.set("")
    
def get_cursor(ev):#decaled variables
    cursor_row=Student_table.focus()
    contents=Student_table.item(cursor_row)
    row=contents['values']
          #print(row)
    mserial.set(row[0])
    mname.set(row[1])
    mrollno.set(row[2])
    myear.set(row[3])
    mcategory.set(row[4])
    mdepartment.set(row[5])
    mdate.set(row[6])
    mstatus.set(row[7])
    mmonth.set(row[8])
    msubjects.set(row[9])
   

         

def update_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="secondyear")
    cur=con.cursor()#  database variables
    cur.execute("update students set name=%s,roll_no=%s,year=%s,category=%s,department=%s,date=%s,status=%s,month=%s,subjects=%s where serial_no=%s",(
                                                                                                                                 mname.get(),
                                                                                                                                 mrollno.get(),
                                                                                                                                 myear.get(),
                                                                                                                                 mcategory.get(),
                                                                                                                                 mdepartment.get(),
                                                                                                                                 mdate.get(),
                                                                                                                                 mstatus.get(),
                                                                                                                                 mmonth.get(),
                                                                                                                                 msubjects.get(),
                                                                                                                                 mserial.get()
                                                                                                                                  ))
 
    con.commit()
    master.withdraw()
    messagebox.showinfo("Information","The record is updated ")
    fetch_data()
    clear_all()
    con.close()
def delete_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="secondyear")
    cur=con.cursor()
    master.withdraw()
    message=messagebox.askyesno("Deletion","Do you want to delete the record")
    if(message>0):
         cur.execute("delete from students where serial_no=%s",mserial.get())
    con.commit()
    con.close()
    fetch_data()
    clear_all()
def search_data():
    con=pymysql.connect(host="localhost",user="root",password="",database="secondyear")
    cur=con.cursor()
    cur.execute("select * from students where "+str(search_by.get())+ " LIKE '%"+str(search_txt.get())+"%'")
    rows=cur.fetchall()
    if(len(rows)!=0):
        Student_table.delete(*Student_table.get_children())
        for row in rows:
            Student_table.insert('',END,values=row)
            con.commit()
    con.close()
def back2():
    
    master.after(10,master.deiconify())
             
#--------------------------------------------------------------------------------------------------------------------


def signup():
    global screen2
    global username1
    global password11
    global confirm_password1
    screen2=Toplevel()
    screen2.title("Sign in ")
    screen2.geometry("1350x700+0+0") #representing width,height,x and y coordinate
    screen2.configure(background="red4")
    screen2.iconbitmap("icon.ico")
    username1=StringVar()
    password11=StringVar()
    confirm_password1=StringVar()
    
        #self.bg_icon=ImageTk.PhotoImage(file="C:\\Users\\AMRITA SINGH JASSAL\\Documents\\background2.jpg")
        #self.bg=Label(screen2,image=self.bg_icon).place(x=0,y=0,relwidth=1)
    frame=Frame(screen2,width=500,height=400,bg="white")
    frame.place(x=450,y=100)
    title=Label(screen2,text="Sign In For New User ",fg="white",bg="black",font=("Times New Roman",30,"bold"),bd=10,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)
    name=Label(frame,text="Username",font=("Times New Roman",15),bg="white",fg="black").grid(row=1,column=0,pady=20,padx=10)
    password=Label(frame,text="Password",font=("Times New Roman",15),bg="white",fg="black").grid(row=2,column=0,pady=20,padx=10)
    cpas=Label(frame,text="Confirm Password",font=("Times New Roman",15),bg="white",fg="black").grid(row=3,column=0,pady=20,padx=10)
    user1=Entry(frame,textvariable=username1,font=("Times New Roman",15),bd=5)
    user1.grid(row=1,column=2,pady=15,padx=10)
    pas11=tk.Entry(frame,textvariable=password11,font=("Times New Roman",15),bd=5)
    pas11.grid(row=2,column=2,pady=15,padx=10)
    confirm_pas2=tk.Entry(frame,textvariable=confirm_password1,show="*",font=("Times New Roman",15),bd=5)
    confirm_pas2.grid(row=3,column=2,pady=15,padx=10)
    button=Button(frame,text="OK",width=10,bd=10,relief=RIDGE,command=save)
    button.grid(row=4,columnspan=3,pady=15,padx=10)
    button1=Button(frame,text="back",width=3,bg="white",bd=0,command=back1)
    button1.grid(row=4,column=5,pady=15,padx=10)

    
def save():
    if(username1.get()=="" or password11.get()=="" or confirm_password1.get()==""):
          master.withdraw()
          messagebox.showinfo("Information","All the fields are required")
    elif( password11.get()!=confirm_password1.get()):
        master.withdraw()
        messagebox.showerror("Error","Passwords do not match")
    else:
        userinfo=username1.get()
        passesinfo=password11.get()
        passessinfo=confirm_password1.get()
        file=open(userinfo,'w')#automatically created
        file.write(userinfo+"\n")
        file.write(passesinfo+"\n")
        file.write(passessinfo)
        file.close()
        master.withdraw()
        messagebox.showinfo("Information","You have successfully sign in !")
def back1():
    screen2.withdraw()
    master.after(10,master.deiconify())
#----------------------------------------------------------------------------------------   
def reset():
    global screen1
    global username
    global password
    global confirm_password
    screen1=Toplevel()
    screen1.title("Reset")
    screen1.geometry("1350x700+0+0") #representing width,height,x and y coordinate
    screen1.configure(background="red4")
    username=StringVar()
    password=StringVar()
    confirm_password=StringVar()
    screen1.iconbitmap("icon.ico")
        #self.bg_icon=ImageTk.PhotoImage(file="C:\\Users\\AMRITA SINGH JASSAL\\Documents\\background2.jpg")
        #self.bg=Label(screen1,image=self.bg_icon).place(x=0,y=0,relwidth=1)
    frame=Frame(screen1,width=500,height=400,bg="white")
    frame.place(x=450,y=100)
    title=Label(screen1,text="Reset Your Details",fg="white",bg="black",font=("Times New Roman",30,"bold"),bd=10,relief=GROOVE)
    title.place(x=0,y=0,relwidth=1)
    name=Label(frame,text="Username",font=("Times New Roman",15),bg="white",fg="black")
    name.grid(row=1,column=0,pady=20,padx=10)
    password1=Label(frame,text="Password",font=("Times New Roman",15),bg="white",fg="black")
    password1.grid(row=2,column=0,pady=20,padx=10)
    cpas=Label(frame,text="Confirm Password",font=("Times New Roman",15),bg="white",fg="black")
    cpas.grid(row=3,column=0,pady=20,padx=10)
    user=Entry(frame,textvariable=username,font=("Times New Roman",15),bd=5)
    user.grid(row=1,column=2,pady=15,padx=10)
    pas1=Entry(frame,textvariable=password,font=("Times New Roman",15),bd=5)
    pas1.grid(row=2,column=2,pady=15,padx=10)
    pas2=Entry(frame,textvariable=confirm_password,show="*",font=("Times New Roman",15),bd=5)
    pas2.grid(row=3,column=2,pady=15,padx=10)
    button=Button(frame,text="Submit",width=10,bd=5,command=okay,relief=RIDGE)
    button.grid(row=4,columnspan=3,pady=15,padx=10)
    button1=Button(frame,text="back",width=3,bg="white",bd=0,command=back)
    button1.grid(row=4,column=5,pady=15,padx=10)
def okay():
   if(username.get()=="" or password.get()=="" or confirm_password.get()==""):
          master.withdraw()
          messagebox.showinfo("Information","All the fields are required")
   elif( password.get()!= confirm_password.get()):
          master.withdraw()
          messagebox.showinfo("Information","Password is incorrect")
   else:
          userinfo1=username.get()
          passesinfo1=password.get()
          passessinfo1=confirm_password.get()
          file=open(userinfo1,'w')
          file.write(userinfo1+"\n")
          file.write(passesinfo1+"\n")
          file.write(passessinfo1)
          file.close()
          master.withdraw()
          messagebox.showinfo("Information","record inserted")

def end():
    messge=messagebox.askokcancel("Information","Do you want to quit the window ?")
    if(messge>0):
        master.after(10,master.destroy())
        
    


def back():
     screen1.withdraw()
     master.after(10,master.deiconify())
def login():
     username_info=us.get()
     password_verify=pas.get()
     confirm_verify=cpassword.get()
     listoffiles=os.listdir("F:\Tkinter")
     if username_info in listoffiles:
          file1=open(username_info,"r")
          verify=file1.read().rstrip()#strips white spaces
          if password_verify in verify and confirm_verify in verify:
               messagebox.showinfo("Information","You have successully signed up!")
               window4()
          else:
               messagebox.showerror("Error","Passwords do not match")
     else:
           messagebox.showerror("Error","Requirements did not match")




          
          
        

#-----------------------------------------------------------------------------------------------  
    
def login_system():
     global master
     global us
     global pas
     global txtuser
     global passuser
     global confirmpas
     global cpas2
     global cpassword
     master=Tk()
     master.title("Login System")
     master.geometry("1350x700+0+0") #representing width,height,x and y coordinate
     master.configure(background="red4")
        #----All images----
        #for inserting image in jpg format we use pillow and for png we will use directly as PhotoImage
        #self.bg_icon=ImageTk.PhotoImage(file="C:\\Users\\AMRITA SINGH JASSAL\\Documents\\background1.jpg")
     logo1=PhotoImage(file="F:\\Tkinter\\user.png")
     user_icon1=ImageTk.PhotoImage(file="F:\\Tkinter\\usericon.jpg")
     pass_icon=PhotoImage(file="F:\\Tkinter\\password1.png")
     master.iconbitmap("icon.ico")

        # ---------variables-----------------
     us=StringVar()
     pas=StringVar()
     cpassword=StringVar()
        
        #if u want to insert a background image then it should be of that size or greater 
        #self.bg=Label(master,image=self.bg_icon).place(x=0,y=0,relwidth=1)
     title=Label(master,text="Login System",font=("Times New Roman",40,"bold"),bg="black",fg="white",bd=10,relief=GROOVE)
     title.place(x=0,y=0,relwidth=1)

     login_frame=Frame(master,bg="white",relief=RIDGE)
     login_frame.place(x=400,y=150)#x=470,y=150)

     logo=Label(login_frame,image=logo1,bd=0).grid(row=0,columnspan=4,pady=10)#column starts from 0 
        
     lglabel=Label(login_frame,text="Username",image=user_icon1,compound=LEFT,font=("Times New Roman",15,"bold"),bg="white").grid(row=1,column=0,padx=10,pady=10)
     txtuser=tk.Entry(login_frame,bd=5,relief=GROOVE,textvariable=us,font=("",15))
     txtuser.grid(row=1,column=2,padx=20,pady=10)#since we r just entering the data so no need of textbox
        
     passlabel=Label(login_frame,text="Password",image=pass_icon,compound=LEFT,font=("Times New Roman",15,"bold"),bg="white").grid(row=2,column=0,padx=10,pady=10)                      
     passuser=tk.Entry(login_frame,bd=5,textvariable=pas,relief=GROOVE,font=("",15))
     passuser.grid(row=2,column=2,padx=20,pady=10)

     confirmpas=Label(login_frame,text="Confirm Password",font=("Times New Roman",15,"bold"),bg="white",fg="black")
     confirmpas.grid(row=3,column=0,pady=10,padx=10)
     cpas2=tk.Entry(login_frame,textvariable=cpassword,show="*",font=("",15),bd=5,relief=GROOVE)
     cpas2.grid(row=3,column=2,pady=10,padx=20)

     btn1=Button(login_frame,text="Login",font=("Times New Roman",10),command=login,width=7,relief=GROOVE,bg="white",fg="black").grid(row=8,column=0,padx=10,pady=15)
        #btn2=Button(login_frame,text="Reset",command=lambda:[self.reset()],font=("Times New Roman",10),width=7,relief=GROOVE,bg="white",fg="black").grid(row=4,column=1)
     btn3=Button(login_frame,text="Quit",font=("Times New Roman",10),width=7,bg="white",command=end,relief=GROOVE,fg="black").grid(row=8,column=3,pady=10,padx=10)
     btn4=Button(login_frame,text="Forgot Password ?",font=("Times New Roman",8),command=reset,bd=0,width=15,bg="white",relief=GROOVE,fg="black").place(x=350,y=380)
     btn5=Button(login_frame,text="Sign up for New User ?",font=("Times New Roman",8),command=signup,bd=0,width=20,bg="white",relief=GROOVE,fg="black").place(x=335,y=400)

     master.mainloop()
      
login_system()
    
        


