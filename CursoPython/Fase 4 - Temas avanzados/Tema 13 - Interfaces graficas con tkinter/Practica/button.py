from struct import pack
from tkinter import *

""" def hola():
    print("Hola Mundo")

def crear_label():
    Label(root, text="label creada dinamicamente").pack() """


def sumar():
    res.set(float(n1.get())+float(n2.get()))
    borrar()


def restar():
    res.set(float(n1.get())-float(n2.get()))
    borrar()


def multiplicar():
    res.set(float(n1.get())*float(n2.get()))
    borrar()


def borrar():
    n1.set("")
    n2.set("")


root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
res = StringVar()

Label(root, text="Numero 1:").pack()
Entry(root, justify="center", textvariable=n1).pack()  # primer num
Label(root, text="Numero 2:").pack()
Entry(root, justify="center", textvariable=n2).pack()  # segundo num
Label(root, text="Suma:").pack()
Entry(root, justify="center", textvariable=res,
      state="disable").pack()  # result

Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Restar", command=restar).pack(side="left")
Button(root, text="Multiplicar", command=multiplicar).pack(side="left")

root.mainloop()
