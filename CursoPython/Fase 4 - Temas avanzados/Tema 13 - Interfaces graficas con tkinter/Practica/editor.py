from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta = ""  # almacenara la ruta de un fichero


def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title(ruta+"Mi editor")


def abrir():
    global ruta
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(initialdir='.', filetypes=(
        ("Ficheros de texto", "*.txt"),), title="Abrir fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, "end")
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta+" - Mi editor")


def guardar():
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        guardarComo()


def guardarComo():
    global ruta
    mensaje.set("Guardar fichero como")
    fichero = FileDialog.asksaveasfile(
        title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""


root = Tk()
root.title("Proyecto editor")

# MENU
menuBar = Menu(root)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Nuevo", command=nuevo)
fileMenu.add_command(label="Abrir", command=abrir)
fileMenu.add_command(label="Guardar", command=guardar)
fileMenu.add_command(label="Guardar como", command=guardarComo)
fileMenu.add_separator()
fileMenu.add_command(label="Salir", command=root.quit)
menuBar.add_cascade(menu=fileMenu, label="Archivo")

# caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

# Monitor inferior
mensaje = StringVar()
mensaje.set("Bienvenido a tu editor de texto")
monitor = Label(root, textvariable=mensaje, justify='left')
monitor.pack(side="left")

root.config(menu=menuBar)

root.mainloop()
