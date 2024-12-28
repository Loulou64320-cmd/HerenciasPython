import os
os.system('cls')


# Superclase o Clase Padre
class Persona():
    # Atributos de clase
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    # metodos dentro de la clase
    def presentarse(self):
        print(f'¡Hola! Me llamo {self.nombre} y tengo {self.edad} años')


# Subclase o Clase Hija
# La clase trabajador hereda los metodos y atributos de la clase persona
class Trabajador(Persona):
    pass


trabajador = Trabajador('Joram', 19, '65478932')
trabajador.presentarse()
print(trabajador.DNI)

persona01 = Persona('Pedro', 49, '0667896513')
persona02 = Persona('Cecilia', 44, '0655689651')

persona01.presentarse()
print(persona01.DNI)

persona02.presentarse()
print(persona02.DNI)
