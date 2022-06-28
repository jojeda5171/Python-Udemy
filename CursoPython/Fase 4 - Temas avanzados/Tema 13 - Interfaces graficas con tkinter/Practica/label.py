from tkinter import *
from tkinter import font

# configuracion de la raiz
root = Tk()

"""
# Variables dinamicas
texto=StringVar()
texto.set("un nuevo texto")

# Configuracion de un marco
# frame=Frame(root,width=480,height=320)
# frame.pack()

Label(root, text="Hola mundo").pack(anchor="nw")
label = Label(root, text="Otra etiqueta")
label.pack(anchor="center")
Label(root, text="Ultima etiqueta").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable=texto)
"""

imagen = PhotoImage(file="img/imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")

# se ejecuta
root.mainloop()
