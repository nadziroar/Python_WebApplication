#import  tkinter modules
from tkinter import *
from tkinter import messagebox
import sqlite3

f = ('Times' , 14)

#For Database CREATE TABLE
con = sqlite3.connect('userdata.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record (
                    name text,
                    email text,
                    contact number,
                    gender text,
                    country text,
                    password text
                )
            ''')
con.commit()

ws = Tk()
ws.title('PythonGuides')
ws.geometry('940x500')
ws.config(bg = '#0B5A81')

def insert_record():
    check_counter = 0
    warn = ""
    if register_name.get() == "":
        warn = "Name can't be empty"
    else:
        check_counter += 1

    if register_email.get() == "":
        warn = "email can't be empty"
    else:
        check_counter += 1

    if register_mobile.get() == "":
        warn = "Contact can't be empty"
    else:
        check_counter += 1

    if var.get() == "":
        warn = "Select Gender"
    else:
        check_counter += 1

    if variable.get() == "":
        warn = "Select Country"
    else:
        check_counter += 1

    if register_pwd.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1

    if pwd_again.get() == "":
        warn = "Re-enter password cant be empty"
    else:
        check_counter += 1

    if register_pwd.get() != pwd_again.get():
        warn = "Password didn't match!"
    else:
        check_counter += 1

    if check_counter == 8 :
        try:
            con = sqlite3.connect('userdata.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES(:name , :email , : contact , :gender, :country , :password)
            ", {


            })
