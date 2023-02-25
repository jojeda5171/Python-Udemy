import sqlite3
from tkinter import *

# Configuracion de la raiz
root = Tk()
root.title("Restaurante")
root.resizable(0, 0)
root.config(bd=25, relief="sunken")

Label(root, text="Restaurante", fg="darkgreen", font=(
    "Times New Roman", 28, "bold italic")).pack()
Label(root, text="Menú del dia", fg="green", font=(
    "Times New Roman", 24, "bold italic")).pack()

# separacion de titulos y contenido
Label(root, text="").pack()

# Conexion a la base de datos
conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# seleccionamos las categorias
categoria = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categoria:
    Label(root, text=categoria[1], fg="black", font=(
        "Times New Roman", 20, "bold italic")).pack()
    platos = cursor.execute(
        "SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=(
            "Verdana", 15, "italic")).pack()

    # separacion de titulos y contenido
    Label(root, text="").pack()

conexion.close()

# precio menu
Label(root, text="12$ (IVA incl.)", fg="darkgreen", font=(
    "Times New Roman", 20, "bold italic")).pack(side="right")

# ejecutamos
root.mainloop()
