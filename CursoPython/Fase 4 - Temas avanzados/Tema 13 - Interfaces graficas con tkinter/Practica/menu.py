from tkinter import *

root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nuevo")
fileMenu.add_command(label="Abrir")
fileMenu.add_command(label="Guardar")
fileMenu.add_command(label="Cerrar")
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)

editMenu = Menu(menuBar, tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="Ayuda")
helpMenu.add_separator()
helpMenu.add_command(label="Acerca de...")

# agrego opciones al menu principal
menuBar.add_cascade(label="Archivo", menu=fileMenu)
menuBar.add_cascade(label="Editar", menu=editMenu)
menuBar.add_cascade(label="Ayuda", menu=helpMenu)

root.mainloop()
