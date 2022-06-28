from tkinter import *

#configuracion de la raiz
root =Tk()
root.title("Hola mundo")
root.iconbitmap("hola.ico")
root.resizable(1,1)

frame=Frame(root,width=480,height=320)
frame.pack(fill='both',expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")

#se ejecuta
root.mainloop()
