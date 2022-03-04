import sys
if len(sys.argv)==3:
    filas=int(sys.argv[1])
    columnas=int(sys.argv[2])
    if filas<1 or filas>9 or columnas<1 or columnas>9:
        print("Error - Filas o columnas incorrectos")
        print("Ejemplo: tabla.py [01-9] [1-0]")
    else:
        #aqui empieza la logica
        for f in range(filas):
            for c in range(columnas):
                print(" * ", end='')
            print()
else:
    print("Error - Argumentos incorrectos")
    print("Ejemplo: tabla.py [1-9] [1-0]")

#print(sys.argv)
