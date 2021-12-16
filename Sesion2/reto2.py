from datetime import date
personas = int(input("¿Cuántas personas ingresan?: "))
lista=[]
for datos in range(0, (personas)): 
    nombre = (input(f"Ingresar nombre de la persona {datos+1} : "))
    dni = (input("Ingresar DNI: "))
    anio = int(input("Ingresar año de nacimiento: "))
    mes = int(input("Ingresar mes de nacimiento: "))
    dia = int(input("Ingresar día de nacimiento: "))

    today = date.today()
    anio2 = (today.year)
    mes2 = (today.month)
    dia2 = (today.day)

    aniofinal = anio2 - anio
    mesfinal = mes2 - mes
    diafinal = dia2 - dia

    if mesfinal <= 0 and diafinal>=0:
        aniofinal = aniofinal -1
    else:
        aniofinal = aniofinal

    resultado = aniofinal

    lista.append(nombre)
    lista.append(dni)
    lista.append(resultado)

# en lista 2 se añaden el contenido de "dato" y aqui se obtiene la lista de edades
lista2=[]

for dato in lista[2:len(lista):3]:
    dato
    lista2.append(int(dato))
# Esta lista2.append(int(dato)) sirve para añadir los datos en numero de las edades en forma de numero

# esta opcion convierte la lista de numeros en una lista ascendente
lista2.sort(key=lambda n: -100/n)
# print(lista2)
# print(lista)

lista3=[]
for dato in lista[2:len(lista):3]:
    lista3.append(int(dato))
    lista3.sort(key=lambda n: -100/n)
# print(lista3)


print("{:^20}{:^20}{:^20}".format("NOMBRES COMPLETOS", "DNI", "EDAD") )
for orden in lista3[0:len(lista3)]:
    print("{:^20}{:^20}{:^20}".format(lista[lista.index(orden) -2], lista[lista.index(orden) -1], lista[lista.index(orden)]) )
