class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def info(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido
        }


# Cuando se hereda, se heredan todas las propiedades y no solo algunas.
# Mediante el (Usuario) se hace mención a qué clase se va a hacer la herencia.
class Alumno(Usuario):
    def __init__(self, Nombre, apellido2, anio, seccion):
        self.anio = anio
        self.seccion = seccion
        # Mediante el metodo super().__init__(nombre, apellido) es que podemos heredas las propiedades de la clase "padre".
        super().__init__(nombre=Nombre, apellido=apellido2)

    def info(self):
        return {
            "nombre": self.nombre,
            "anio": self.anio,
            "apellido": self.apellido,
            "seccion": self.seccion
        }


alumnoEduardo = Alumno("Eduardo", "de Rivero", "Sexto", "A")
usuarioRaul = Usuario("Raul", "Mendoza")

informacion = alumnoEduardo.info()
print(informacion)
print(usuarioRaul.info())
