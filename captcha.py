import random
from tkinter import*
root=Tk()
root.title("CATPTCHA check")
root.geometry("500x500")
p="1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
global k
global b
b=0
root.config(background="#ffffe0")
key=StringVar()
k="".join(random.sample(p,4))
key.set(k)
bf=Frame(root).grid()
Label(root,text="Captcha :",bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold").grid(column=4,row=1)
e5=Entry(root,textvariable=key)
e5.grid(column=4,row=2)
l2= Label(root,text="ENTER Captcha" ,bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold")
l2.grid(column=4,row=3)
global a
a=0
def click():
    l=e2.get()
    if(l==k):
        global l4
        global b
        b=1
        l4=Label(root,text="continue",bg="#98FB98", fg="#033", font="verdana 12 bold")
        l4.grid(column=8,row=3)
    else:
        global l5
        global a
        a=1
        l5=Label(root,text="Give the correct captcha",bg="#98FB98", fg="#033", font="verdana 12 bold")
        l5.grid(column=8,row=6)
def cl():
    global k
    k="".join(random.sample(p,4))
    key.set(k)
    e5=Entry(root,textvariable=key)
    e5.grid(column=4,row=2)
    global l3
def cli():
    if (b==1):
        l4.destroy()
    if(a==1):
        l5.destroy()
    e2.delete(0,END)
var=StringVar()
e2= Entry(root,textvariable=var,width=20)
e2.grid(column=4,row=6)

Button(root,text="Submit",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=click).grid(column=3,row=7)
Button(root,text="Refresh",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=cl).grid(column=4,row=7)
Button(root,text="Clear",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=cli).grid(column=7,row=7)

root.mainloop()
