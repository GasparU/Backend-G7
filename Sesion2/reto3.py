# Este es el reto 2 de Mamani Yanapa, Wilson

# Librería para ordenar diccionarios en listas
from operator import itemgetter

# Ingreso de datos de personas
get_people = int(input("¿Ingrese el número de personas?: "))
allPeopleList=[]
for nPeople in range(0, get_people): 
  name = (input(f"Por favor, ingrese el nombre de la persona {nPeople+1} : "))
  dni = (input("Ingrese DNI: "))
  bday = (input("Ingrese la fecha de nacimiento en formato aaaa/mm/dd: "))
  allPeopleList.append({
    "name": name,
    "dni": dni,
    "birthday" : bday
    })

# Orden de diccionarios según la fecha de nacimiento
allPeopleList.sort(key=itemgetter('birthday'))

# Impresión de ascendente de personas según su fecha de nacimiento
print(' ')
print('Estas son las personas de más joven a mayor:')
print('============================================')
print(' Nombre  |  DNI   | Fecha de Nacimiento')
print('-------------------------------------------')
for people in allPeopleList:
  print(people['name'],'    ',people['dni'],'    ',people['birthday'])
  print('-------------------------------------------')