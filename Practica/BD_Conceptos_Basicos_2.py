import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# cursor.execute('''
# CREATE TABLE usuarios (
# dni VARCHAR(10) PRIMARY KEY,
# nombre VARCHAR(100),
# edad INTEGER,
# email VARCHAR(100)
# )
# ''')

# usuarios = [('1850435171', 'Jose', 24, 'jojeda5171@uta.edu.ec'),
#            ('1234567890', 'Andres', 21, 'dsuvhudjvbn'),
#            ('0987654321', 'Luis', 24, 'nughbkjl'),
#            ('1122334455', 'Maria', 25, 'nugjvbn'), ]
#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

""" cursor.execute('''
CREATE TABLE productos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre VARCHAR(100) NOT NULL,
marca VARCHAR(50) NOT NULL,
precio FLOAT NOT NULL
)''') """

""" productos = [('Teclado', 'Logitech', 25.5),
            ('Mouse', 'Logitech', 15.5),
            ('Monitor', 'Samsung', 250.5),
            ('Audifonos', 'Sony', 50.5), ] """

#cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)

""" cursor.execute("SELECT * FROM productos")
print(cursor.fetchall()) """

cursor.execute('''
CREATE TABLE usuarios(
id INTEGER PRIMARY KEY AUTOINCREMENT,
dni VARCHAR(10) UNIQUE NOT NULL,
nombre VARCHAR(100) NOT NULL,
edad INTEGER NOT NULL,
email VARCHAR(100) NOT NULL
)''')
usuarios = [('1850435171', 'Jose', 24, 'jojeda5171@uta.edu.ec'),
            ('1234567890', 'Andres', 21, 'dsuvhudjvbn'),
            ('0987654321', 'Luis', 24, 'nughbkjl'),
            ('1122334455', 'Maria', 25, 'nugjvbn')]
cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)", usuarios)

conexion.commit()
conexion.close()
