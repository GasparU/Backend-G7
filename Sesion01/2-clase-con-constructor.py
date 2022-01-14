class Vehiculo:
    """Clase que sirve para el uso de los vehiculos"""
    def __init__(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        self.__velocidad = 0
    
    def acelerar(self):
        """Metodo que acelera el vehiculo de 20 en 20"""
        self.__velocidad +=20
        return 'la velocidad actual es: {} km/h' .format(self.__velocidad)
    
    def desacelerar(self):
        """Metodo que desacelera el vehiculo de 20 en 20"""
        self.__velocidad -=20

vehiculo1 = Vehiculo('azul', 'x3', '4x2')

print(vehiculo1.__velocidad())





print(vehiculo1.acelerar())
print(vehiculo1.acelerar())