from doctest import master
from idlelib.multicall import r
from tkinter import Tk, Label, IntVar, Radiobutton, END
from turtle import rt

import el
import mysql.connector
from tkinter import messagebox

import mysql.connector
import rooot

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sangam",
    database="dbl"
)
cur = mydb.cursor()
s = "CREATE TABLE IF NOT EXISTS EmpApp(EmpNo integer(4),EmpName var"
cur.execute(s)


def loginQuit():
    ask = messagebox.askyesno("Quitting", "Are you sure you want to Quit")
    if ask == True:
        master.destroy()


def user_valid():
    v = ery2.get()
    n = ery3.get()
    if v.lower() == "sangam" and n == "sangam":
        master.destroy()
        root = Tk()
        root.title("Employee Management System")
        w = 550
        h = 500
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        # calculate position x, y
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(0, 0)
        root.configure(bg="black")

        lbll = Label(root, text="Select Your Choice", relief="")
        lbll.place(x=140, y=20)

        global var
        var = IntVar()
        R1 = Radiobutton(root, variable=var, bg="black", value=1, )
        R1.place(x=160, y=100)

        R2 = Radiobutton(root, variable=var, bg="black", value=2, )

        R2.place(x=160, y=160)
        R3 = Radiobutton(root, variable=var, bg="black", value=3, )
        R3.place(x=160, y=220)

        R4 = Radiobutton(root, variable=var, bg="black", value=4, )
        R4.place(x=160, y=280)
        R5 = Radiobutton(root, variable=var, bg="black", value=5, )
        R5.place(X=160, Y=340)

        R6 = Radiobutton(root, variable=var, bg="black", value=6, )

        R6.place(x=160, y=400)

        lbl2 = Label(root, text="Add Employee", font="Arial 15 bold")
        lbl2.place(x=190, y=100)

        lbl3 = Label(root, text="Search Employee", font="Arial 15 bold")
        lbl3.place(x=190, y=160)

        lbl4 = Label(root, text="Show All Employees", font="Arial 15 bold")
        lbl4.place(x=190, y=220)

        lbl5 = Label(root, text="Update Employee", font="Arial 15 bold")
        lbl5.place(x=190, y=280)

        lbl6 = Label(root, text="Delete Employee", font="Arial 15 bold")
        lbl6.place(x=190, y=340)

        lbl7 = Label(root, text="Quit", font="Arial 15 bold", bg="black")
        lbl7.place(x=190, y=400)
    else:
        messagebox.showerror("Error", "Wrong UserName or Password")

    def addemp(e1=None, e2=None, e3=None):

        try:
            a = int(el.get())
            b = e2.get()
            c = float(e3.get())

            if b == "":
                messagebox.showinfo("Required", "Please Input All Field")
            else:

                cur = mydb.cursor()
                s = "INSERT INTO EmpApp(EmpNo,EmpName,EmpSal) VALUES(%S,%)"
                b1 = (a, b, c)
                cur.execute(s, b1)
                mydb.commit()

        except ValueError:
            messagebox.showinfo("Error", "Please Input in Correct Way")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.focus()


def closescrn1():
    rt.destroy()


def closescrn2():
    rot.destroy()
def closescrn3():
    rooot.destroy

def closescrn4(roooot=None):
    roooot.destroy
def closescrn5():
    r.destroy