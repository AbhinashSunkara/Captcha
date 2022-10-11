import random
from tkinter import*
root=Tk()
root.title("CATPTCHA check")
root.geometry("800x800")
p="1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
global k
global b
b=0
root.config(background="#ffffe0")
key=StringVar()
k="".join(random.sample(p,4))
key.set(k)
bf=Frame(root).grid()
l1=Label(root,text="Captcha :",bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold")
l1.place(relx=0.4,rely=0.3,anchor=CENTER)
e5=Entry(root,textvariable=key)
e5.place(relx=0.4,rely=0.35,anchor=CENTER)
l2= Label(root,text="ENTER Captcha" ,bg="#2C3E50", fg="#EAECEE", font="verdana 10 bold")
l2.place(relx=0.4,rely=0.4,anchor=CENTER)
global a
a=0
def click():
    l=e2.get()
    if(l==k):
        global l4
        global b
        b=1
        l4=Label(root,text="continue",bg="#98FB98", fg="#033", font="verdana 12 bold")
        l4.place(relx=0.7,rely=0.3,anchor=CENTER)
    else:
        global l5
        global a
        a=1
        l5=Label(root,text="Give the correct captche",bg="#98FB98", fg="#033", font="verdana 12 bold")
        l5.place(relx=0.7,rely=0.3,anchor=CENTER)
def cl():
    global k
    k="".join(random.sample(p,4))
    key.set(k)
    e5=Entry(root,textvariable=key)
    e5.place(relx=0.4,rely=0.35,anchor=CENTER)
    global l3
def cli():
    if (b==1):
        l4.destroy()
    if(a==1):
        l5.destroy()
    e2.delete(0,END)
var=StringVar()
e2= Entry(root,textvariable=var,width=20)
e2.place(relx=0.4,rely=0.45,anchor=CENTER)

Button(root,text="Submit",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=click).place(relx=0.3,rely=0.5,anchor=CENTER)
Button(root,text="Refresh",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=cl).place(relx=0.43,rely=0.5,anchor=CENTER)
Button(root,text="Clear",bg="#fdde6c", fg="#000", font="verdana 12 bold",command=cli).place(relx=0.54,rely=0.5,anchor=CENTER)

root.mainloop()
