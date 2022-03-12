from io import open
import pickle


class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.defensa = defensa
        self.ataque = ataque
        self.alcance = alcance

    def __str__(self):
        return "{} -> {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre, self.vida, self.defensa, self.ataque, self.alcance)


###
class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Gestor:

    personajes = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self, p):
        for pTemp in self.personajes:
            if pTemp.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()

    def borrar(self, nombre):
        for pTemp in self.personajes:
            if pTemp.nombre == nombre:
                self.personajes.remove(pTemp)
                self.guardar()
                print("\nPersonaje {} borrado".format(nombre))
                return

    def mostrar(self):
        if len(self.personajes) == 0:
            print("gestor esta vacio")
            return
        for p in self.personajes:
            print(p)

    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            #print("El fichero esta vacio")
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))

    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.personajes, fichero)
        fichero.close()
        del(fichero)


G = Gestor()
G.mostrar()

#G.agregar(Personaje("Caballera", 4, 2, 4, 2))
#G.agregar(Personaje("Guerrero", 2, 4, 2, 4))
#G.agregar(Personaje("Arquero", 2, 4, 1, 8))
#G.mostrar()

G.borrar("Arquero")
G.borrar("Caballera")
G.mostrar()
