class Vehiculo: 
    ruedas = 4
    color = 'azul'

vehiculo1 = Vehiculo()
vehiculo1.ruedas = 7
# Se puede agregar atributos que no estan en la clase, como el caso de "procedencia", pero solo afectara a vehiculo1, no a los demás objetos.
# Pero, esto no es una buena práctica, porque se debe preferir el objeto integro y no añadir particularidades
vehiculo1.procedencia = 'Japón'

vehiculo2 = Vehiculo()

# print(vehiculo1.ruedas)
# print(vehiculo2.ruedas)
# print(vehiculo1.procedencia)


class VehiculoConConstructor():
    # en todo metodo de la clase, SIEMPRE tendremos que colocar como primer parametro la palabra "self"
    # self: sirve para referenciar a la instancia actual de la clase, esto se podría comparar con el uso de this
    def __init__(self, ruedas, color):
        self.ruedas = ruedas
        self.color = color
    
    def __str__(self):
        return 'Esta es una instancia de VehiculoConConstructor'

vehiculo3 = VehiculoConConstructor(18, 'celeste')
print(vehiculo3)