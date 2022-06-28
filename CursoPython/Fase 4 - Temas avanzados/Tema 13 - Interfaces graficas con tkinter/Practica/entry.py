from tkinter import *

# Configuracion de la raiz
root = Tk()

entry = Entry(root)
entry.grid(row=0, column=1, sticky="e", padx=5, pady=5)
entry.config(justify="right", state="disabled")

label = Label(root, text="Nombredddddddddd")
label.grid(row=0, column=0)

entry2 = Entry(root)
entry2.grid(row=1, column=1)
entry2.config(show="?")

label2 = Label(root, text="Contraseña")
label2.grid(row=1, column=0, sticky="e", padx=5, pady=5)


# Se ejecuta
root.mainloop()
