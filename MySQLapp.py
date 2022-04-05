# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:23:18 2022

@author: hp
"""
import tkinter as tk
from PIL import Image , ImageTk
import tkinter as tk
from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox

import mysql.connector
import pandas as pd
db=mysql.connector.connect(host='localhost',password='1234',user='root',database='sql_store')
if db.is_connected():
    print('connection established')
    
def show_customers():
    df=pd.read_sql('SELECT * FROM customers',db)
    return df
def display0():
    root=tk.Tk()
    
    canvas0=tk.Canvas(root,height=500,width=500)
    canvas0.pack()
    
    frame0=tk.Frame(root,bg='#80c1ff',bd=10)
    frame0.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.6,anchor='n')
    
    label0=tk.Label(frame0)
    label0.place(relwidth=1,relheight=1)
    
    label0['text']=show_customers()
    root.mainloop()

    
def show_orders():
    df=pd.read_sql('SELECT * FROM orders',db)
    return df
def display1():
    root=tk.Tk()
    
    canvas1=tk.Canvas(root,height=500,width=500)
    canvas1.pack()
    
    frame1=tk.Frame(root,bg='#80c1ff',bd=10)
    frame1.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.6,anchor='n')
    
    label1=tk.Label(frame1)
    label1.place(relwidth=1,relheight=1)
    label1['text']=show_orders()
    
    root.mainloop()
    

def open_file():

    filename=filedialog.askopenfilename(initialdir='/',title ='selectfile',filetypes=(('executables','*.exe'),('all files','*.*')))
    apps.append(filename)
    
    for app in apps:
        label=tk.Label(frame_lower, text=app, bg='gray')
        label.pack()
    
def run_app():
    for app in apps:
        os.startfile(app)
def display2():
    
    label1['text']=open_file()
    
def show_join():
    df=pd.read_sql('SELECT * FROM customers JOIN orders USING(customer_id)',db)
    return df
    root.mainloop()
def display3():
    root=tk.Tk()
   
    canvas3=tk.Canvas(root,height=500,width=500)
    canvas3.pack()
    frame3=tk.Frame(root,bg='#80c1ff',bd=10)
    frame3.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.6,anchor='n')
    
    label3=tk.Label(frame3)
    label3.place(relwidth=1,relheight=1)
    
    label3['text']=show_join()
    root.mainloop()
    
def show_tables():
    root=tk.Tk()
    
    canvas4=tk.Canvas(root,height=300,width=300)
    canvas4.pack()
    
    frame4=tk.Frame(root,bg='#80c1ff',bd=10)
    frame4.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.3,anchor='n')
    
    label4=tk.Label(frame4)
    label4.place(relwidth=1,relheight=1)
    
    btn8= tk.Button(frame4,text='customer',bg='#263D42',fg='white',command=display0) 
    btn8.place(relx=0.1,relheight=0.3,relwidth=0.3)
    
    btn7= tk.Button(frame4,text='orders',bg='#263D42',fg='white',command=display1) 
    btn7.place(relx=0.6,relheight=0.3,relwidth=0.3)
    
    root.mainloop()
   
def insert_rows():
    root=tk.Tk()
    
    canvas4=tk.Canvas(root,height=300,width=300)
    canvas4.pack()
    
    frame4=tk.Frame(root,bg='#80c1ff',bd=10)
    frame4.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.3,anchor='n')
    
    label4=tk.Label(frame4)
    label4.place(relwidth=1,relheight=1)
    
    btn8= tk.Button(frame4,text='customer',bg='#263D42',fg='white',command=insert_customers) 
    btn8.place(relx=0.1,relheight=0.3,relwidth=0.3)
    
    btn7= tk.Button(frame4,text='orders',bg='#263D42',fg='white',command=display1) 
    btn7.place(relx=0.6,relheight=0.3,relwidth=0.3)
    
    root.mainloop()
    
def order_by():
    df=pd.read_sql('SELECT * FROM customers ORDER BY points DESC',db)
    return df
    root.mainloop()
def display4():
    root=tk.Tk()
   
    canvas3=tk.Canvas(root,height=500,width=500)
    canvas3.pack()
    frame3=tk.Frame(root,bg='#80c1ff',bd=10)
    frame3.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.6,anchor='n')
    
    label3=tk.Label(frame3)
    label3.place(relwidth=1,relheight=1)
    
    label3['text']=order_by()
    root.mainloop()

    
    
def insert_customers():
    root=tk.Tk()
    l=[]
    
    canvas4=tk.Canvas(root,height=400,width=400)
    canvas4.pack()
    
    frame4=tk.Frame(root,bg='white',bd=10)
    frame4.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.8,anchor='n')
    
    l1=tk.Label(frame4,text='customer_id')
    l1.grid(row=0,column=0)
    
    entry1=Entry(frame4)
    
    entry1.grid(row=0,column=1)
    def save_customer_id():
        text=entry1.get()
        l.append(text)
        
    
    btn15=Button(frame4,text='update',command=save_customer_id)
    btn15.grid(row=0,column=2)
    
    l1=tk.Label(frame4,text='first_name')
    l1.grid(row=1,column=0)
    
    entry2=Entry(frame4)
    entry2.grid(row=1,column=1)
    
    def save_first_name():
        text2=entry2.get()
        l.append(text2)
        
        
    
    btn16=Button(frame4,text='update',command=save_first_name)
    btn16.grid(row=1,column=2)
    
    l1=tk.Label(frame4,text='last_name')
    l1.grid(row=2,column=0)
    
    entry3=Entry(frame4)
    entry3.grid(row=2,column=1)
    def save_last_name():
        text3=entry3.get()
        l.append(text3)
    
    btn17=Button(frame4,text='update',command=save_last_name)
    btn17.grid(row=2,column=2)
    
    l1=tk.Label(frame4,text='birth_date')
    l1.grid(row=3,column=0)
    
    entry4=Entry(frame4)
    entry4.grid(row=3,column=1)
    def save_birth_date():
        text4=entry4.get()
        l.append(text4)
    
    btn18=Button(frame4,text='update',command=save_birth_date)
    btn18.grid(row=3,column=2)
    
    l1=tk.Label(frame4,text='phone')
    l1.grid(row=4,column=0)
    
    entry5=Entry(frame4)
    entry5.grid(row=4,column=1)
    def save_phone():
        text5=entry5.get()
        l.append(text5)
    
    btn19=Button(frame4,text='update',command=save_phone)
    btn19.grid(row=4,column=2)
    
    l2=tk.Label(frame4,text='address')
    l2.grid(row=5,column=0)
    
    entry6=Entry(frame4)
    entry6.grid(row=5,column=1)
    def save_address():
        text6=entry6.get()
        l.append(text6)
    
    btn20=Button(frame4,text='update',command=save_address)
    btn20.grid(row=5,column=2)
    
    l1=tk.Label(frame4,text='city')
    l1.grid(row=6,column=0)
    
    entry7=Entry(frame4)
    entry7.grid(row=6,column=1)
    def save_city():
        text7=entry7.get()
        l.append(text7)

    
    btn18=Button(frame4,text='update',command=save_city)
    btn18.grid(row=6,column=2)
    
    l1=tk.Label(frame4,text='state')
    l1.grid(row=7,column=0)
    
    entry8=Entry(frame4)
    entry8.grid(row=7,column=1)
    def save_state():
        text8=entry8.get()
        l.append(text8)
    btn18=Button(frame4,text='update',command=save_state)
    btn18.grid(row=7,column=2)
    
    l1=tk.Label(frame4,text='points')
    l1.grid(row=8,column=0)
    
    entry9=Entry(frame4)
    entry9.grid(row=8,column=1)
    def save_points():
        text9=entry9.get()
        l.append(text9)
        
    
    btn18=Button(frame4,text='update',command=save_points)
    btn18.grid(row=8,column=2)
    
    
    
    #label4=tk.Label(frame4)
    #label4.place(relwidth=1,relheight=1)
    def confirm():
        c1=db.cursor()
        flist=(l)
        print(flist)
        sql='''INSERT INTO customers (customer_id,first_name,last_name,birth_date,phone,address,city,state,points)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        c1.execute(sql,flist)
        db.commit()
        
    btn21=Button(frame4,text='confirm',command=confirm)
    btn21.grid(row=9,column=2)
    
    root.mainloop()
    
    

    
    
def sql_operations():
    root=tk.Tk()
    
    canvas4=tk.Canvas(root,height=300,width=300)
    canvas4.pack()
    
    frame4=tk.Frame(root,bg='#80c1ff',bd=10)
    frame4.place(relx=0.5,rely=0.25,relwidth=0.9,relheight=0.3,anchor='n')
    
    label4=tk.Label(frame4)
    label4.place(relwidth=1,relheight=1)
    
    btn6= tk.Button(frame4,text='show tables',bg='#263D42',fg='white',command=show_tables) 
    btn6.place(relx=0.1,relheight=0.3,relwidth=0.3)
    
    btn9= tk.Button(frame4,text='join tables',bg='#263D42',fg='white',command=display3) 
    btn9.place(relx=0.6,relheight=0.3,relwidth=0.3)
    
    btn10= tk.Button(frame4,text='insert rows',bg='#263D42',fg='white',command=insert_rows) 
    btn10.place(relx=0.1,rely=0.4,relheight=0.3,relwidth=0.3)
    
    btn10= tk.Button(frame4,text='order by',bg='#263D42',fg='white',command=display4) 
    btn10.place(relx=0.6,rely=0.4,relheight=0.3,relwidth=0.3)
    
    root.mainloop()



       

root=tk.Tk()
apps=[]

canvas=tk.Canvas(root,width=1366, height=768)
canvas.grid(columnspan=3)


background_image=tk.PhotoImage(master=canvas,file='background.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

#sql_image=tk.PhotoImage(master=canvas,file='sqllogo.png')
#sql_label=tk.Label(root,image=sql_image)
#sql_label.place(relwidth=1,relheight=1)


#background=Image.open('background.jpg')
#background=ImageTk.PhotoImage(background)
#background_label=tk.Label(image=background)
#background_label.image=background
#background_label.grid(column=1)
#background_label.place(x=0,y=0,relwidth=1,relheight=1)

frame=tk.Frame(root,bg='#f2f5f2',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.45,relheight=0.6,anchor='n')


#entry=tk.Entry(frame,font=40)
#entry.place(relwidth=0.65,relheight=1)


#btn = tk.Button(frame,text='customer',bg='#263D42',fg='white',command=display0) 
#btn.place(relx=0.3,relheight=0.3,relwidth=0.1)

#btn1= tk.Button(frame,text='orders',bg='#263D42',fg='white',command=display1) 
#btn1.place(relx=0.2,relheight=0.3,relwidth=0.1)

btn2= tk.Button(frame,text='open file',bg='#263D42',fg='white',command=display2) 
btn2.place(relx=0.45,rely=0.4,relheight=0.1,relwidth=0.1)

#btn3= tk.Button(frame,text='join',bg='#263D42',fg='white',command=display3) 
#btn3.place(relx=0,relheight=0.3,relwidth=0.1)

btn4= tk.Button(frame,text='run app',bg='#263D42',fg='white',command=run_app) 
btn4.place(relx=0.45,rely=0.5,relheight=0.1,relwidth=0.1)

btn5= tk.Button(frame,text='sql operations',bg='#263D42',fg='white',command=sql_operations )
btn5.place(relx=0.43,rely=0.85,relheight=0.1,relwidth=0.15)



frame_lower=tk.Frame(root,bg='#80c1ff',bd=10)
frame_lower.place(relx=0.5,rely=0.7,relwidth=0.45,relheight=0.1,anchor='n')

logo=PhotoImage(file='mysql.png')
sql_label=Label(frame,image=logo)
sql_label.place(relx=0.36,rely=0)

instruction=tk.Label(frame, text='To open your MySQL database click open file to copy path and then click run app',font='Helvetica')
instruction.place(relx=0.05,rely=0.3)

instruction1=tk.Label(frame, text='To work with your database click sql operations',font='Helvetica')
instruction1.place(relx=0.23,rely=0.75)

label=tk.Label(frame_lower)
label.place(relwidth=1,relheight=1)



root.mainloop()
 



