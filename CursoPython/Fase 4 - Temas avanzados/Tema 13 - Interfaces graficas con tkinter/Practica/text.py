from tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
""" tamaño se basa en el mumero de lineas y caracteres """
texto.config(width=30, height=10, font=("Consolas", 12),
             padx=15, pady=15, selectbackground="red")

root.mainloop()
