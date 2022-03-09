class Pelicula:
    # constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("se ha crado la pelicula", self.titulo)

    # Destructor
    def __del__(self):
        print("Se esta borrando la pelicula", self.titulo)

p = Pelicula("El Padrino", 172, 1972)
del (p)

