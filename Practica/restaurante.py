import sqlite3


def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    try:
        cursor.execute('''
        CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)
            ''')
    except sqlite3.OperationalError:
        print("La tabla categoria ya existe")
    else:
        print("Se ha creado la tabla categoria")

    try:
        cursor.execute('''CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))
            ''')
    except sqlite3.OperationalError:
        print("La tabla plato ya existe")
    else:
        print("Se ha creado la tabla plato")

    conexion.close()


def agregar_categoria():
    categoria = input("Ingrese el nombre de la categoria: ")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute(
            "INSERT INTO categoria VALUES (null,'{}')".format(categoria))
    except sqlite3.IntegrityError:
        print("La categoria {} ya existe".format(categoria))
    else:
        print("Se ha agregado la categoria {}".format(categoria))

    conexion.commit()
    conexion.close()


def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categorias = cursor.execute("SELECT * FROM categoria").fetchall()
    print("Seleccione una categoria para el plato:")
    for categoria in categorias:
        print("[{}] {}".format(categoria[0], categoria[1]))

    categoria_usuario=int(input(">"))
    nombre_plato = input("Ingrese el nombre del plato: ")
    try:
        cursor.execute(
            "INSERT INTO plato VALUES (null,'{}', {})".format(nombre_plato, categoria_usuario))
    except sqlite3.IntegrityError:
        print("El plato {} ya existe".format(nombre_plato))
    else:
        print("Se ha agregado el plato {}".format(nombre_plato))
    conexion.commit()
    conexion.close()

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    categoria=cursor.execute("SELECT * FROM categoria").fetchall()
    for categoria in categoria:
        print("[{}] {}".format(categoria[0], categoria[1]))
        platos=cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
        for plato in platos:
            print("    [{}] {}".format(plato[0], plato[1]))


    conexion.close()


# Crear la BD
crear_bd()

# Menu de opciones
while True:
    print("\nBienvenido al restaurante")
    opcion = input(
        "\nIngrese una opcion:\n[1] Agregar una categoria\n[2] Agregar un plato\n[3] Mostrar Menú \n[4] Salir del programa\n\n>")

    if opcion == "1":
        agregar_categoria()
    elif opcion == "2":
        agregar_plato()
    elif opcion == "3":
        mostrar_menu()
    elif opcion == "4":
        print("Gracias por usar el programa")
        break
    else:
        print("Opcion incorrecta")
