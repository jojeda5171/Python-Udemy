import math
import random
import random

def leer_numero(ini,fin,sms):
    while True:
        try:
            valor=int(input(sms))
        except:
            print("Error: numero no valido")
        else:
            if valor>=ini and valor<=fin:
                break
    return valor

def generador():
    numeros=leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo=leer_numero(1,3,"¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista=[]

    for i in range(numeros):
        numero=random.uniform(0,101)
        
        if modo==1:
            print("{} --> {}".format(numero,math.ceil(numero)))
            numero=math.ceil(numero)
        elif modo==2:
            print("{} --> {}".format(numero,math.floor(numero)))
            numero=math.floor(numero)
        elif modo==3:
            print("{} --> {}".format(numero,round(numero)))
            numero=round(numero)
        else:
            print("Error: opcion no valida")

        lista.append(numero)
generador()