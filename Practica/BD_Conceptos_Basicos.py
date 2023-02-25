import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

#cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
#cursor.execute("INSERT INTO usuarios VALUES ('Luis', 24, 'lojeda5171@uta.edu.ec')")
#datos=cursor.execute("SELECT * FROM usuarios")
# print(datos.fetchall())

usuarios = [('Andres', 21, 'dsuvhudjvbn'),
            ('Luis', 24, 'nughbkjl'),
            ('Maria', 25, 'nugjvbn'), ]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)

print(cursor.execute("SELECT * FROM usuarios").fetchone())

conexion.commit()

conexion.close()
