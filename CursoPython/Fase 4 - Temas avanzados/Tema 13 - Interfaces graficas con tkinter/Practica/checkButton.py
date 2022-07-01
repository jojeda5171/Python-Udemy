from email.mime import image
from tkinter import *


def seleccionar():
    cadena = ""
    if(leche.get()):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if(azucar.get()):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"

    monitor.config(text=cadena)


root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = IntVar()
azucar = IntVar()

imagen = PhotoImage(file="img/imagen.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿Cómo quieres el café?").pack(anchor="w")
Checkbutton(frame, text="Con leche", variable=leche,
            onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")
Checkbutton(frame, text="Con azúcar", variable=azucar,
            onvalue=1, offvalue=0, command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()
