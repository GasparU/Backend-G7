nombre = input("¿Cuál es su nombre? : ")
edad = int(input("¿Cuál es su edad? : "))

import time
time.localtime()
hora = time.strftime("%H")
minutos = time.strftime("%M")
# if edad < 18 && time.strftime("%H") < 18
respuesta = "Ve a dormir" if edad <18 and time.strftime("%H") > "5" else "Ve a hacer la tarea"
if (edad < 18 and int(hora) < 18):
    print(f"Hola, {nombre}, son las {hora}:{minutos} horas y debes hacer la tarea")
elif (edad < 18 and int(hora) > 18):
    print(f"Hola, {nombre}, ya son las {hora}:{minutos} horas y debes ir a dormir")
elif (edad >= 18 and int(hora) > 18):
    print(f"Hola {nombre}, son las {hora}:{minutos} horas y no estas obligado a hacer nada")