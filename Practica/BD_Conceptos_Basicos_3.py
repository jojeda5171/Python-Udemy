import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

#cursor.execute("UPDATE usuarios SET nombre = 'Luis Ojeda', edad=50 WHERE dni = '0987654321'")
cursor.execute("DELETE FROM  usuarios WHERE dni = '0987654321'")

conexion.commit()
conexion.close()