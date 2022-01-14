class Vehiculo:
    """Clase que sirve para el uso de los vehiculos"""
    def __init__(self, color, modelo, traccion):
        self.color = color
        self.modelo = modelo
        self.traccion = traccion
        self.velocidad = 0
    
    def acelerar(self):
        """Metodo que acelera el vehiculo de 20 en 20"""
        self.velocidad +=20
        return 'la velocidad actual es: {} km/h' .format(self.velocidad)
    
    def desacelerar(self):
        """Metodo que desacelera el vehiculo de 20 en 20"""
        self.velocidad -=20

class VehiculoVolador(Vehiculo):
    def __init__(self, color, modelo, traccion, vuela= False):
       super().__init__(color, modelo, traccion)
       self.vuela = vuela
    
    def volar(self):
        self.vuela = True
    
    def aterrizar(self):
        self.vuela = False
    
    def estado(self):
        return 'el vehiculo es de color: {}, modelo: {}, tracción: {}, velocidad: {}km/h y está {}'

class VehiculoOffRoad(VehiculoVolador):
    def __init__(self, color, modelo, traccion, vuela=False, sumergido=False):
        super().__init__(color,modelo,traccion, vuela)


obj_vehiculo = Vehiculo('verde','rx5', '4x4')
obj_vehiculo_volador = VehiculoVolador('blanco','xyz','4x2')
obj_vehiculo_volador.volar()
# print(obj_vehiculo_volador.vuela)
# print(obj_vehiculo_volador.color)

# print(obj_vehiculo.vuela)
vehiculo2 = Vehiculo('Azul', 'Ferrari', '4x2')
print(vehiculo2.estado)

obj_vehiculo_offroad = VehiculoOffRoad('azul','asda','4x2')
obj_vehiculo_offroad.acelerar()
obj_vehiculo_offroad.desacelerar()
obj_vehiculo_offroad.volar()

