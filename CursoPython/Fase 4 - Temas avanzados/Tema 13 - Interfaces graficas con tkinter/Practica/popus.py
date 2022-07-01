from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as Colorchooser
from tkinter import filedialog as FileDialog

root = Tk()


def test():
    # MessageBox.showinfo("Titulo","Hola mundo")
    # MessageBox.showwarning("Titulo","Acceso denegado")
    # MessageBox.showerror("Titulo","Error")
    """ resultado = MessageBox.askquestion(
        "Titulo", "¿Estas seguro que quieres salir sin guardar?")
    if(resultado == "yes"):  # no
        root.destroy() """
    """ resultado = MessageBox.askokcancel(
        "Titulo", "¿Quieres sobreescribir?")
    if(resultado == True):  # false
        root.destroy() """
    """ resultado = MessageBox.askyesno(
        "Titulo", "¿Quieres sobreescribir?")
    if(resultado):  # no
        root.destroy()  """
    """ resultado = MessageBox.askretrycancel("Titulo", "No se puede conectar")
    if(resultado == False):  # no
        root.destroy() """

    #color=Colorchooser.askcolor(title="Elige un color")
    # print(color)

    """ ruta = FileDialog.askopenfilename(title="Abrir un fichero", initialdir="D:", filetypes=(
        ("Ficheros de texto", "*.txt"), ("Ficheros de texto avanzado", "*.txt2"), ("Todos los Ficheros de texto", "*.*")))
    print(ruta) """

    # equivale a open('ruta', 'w')
    fichero = FileDialog.asksaveasfile(
        title="Guardar un archivo", mode="w", defaultextension=".txt")
    if(fichero is not None):
        fichero.write("Hola mundo")
        fichero.close()
    print(fichero)


Button(root, text="Clicame", command=test).pack()

root.mainloop()
