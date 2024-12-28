class Persona():
    # Atributos de clase
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    # metodos dentro de la clase
    def presentarse(self):
        print(f'¡Hola! Me llamo {self.nombre} y tengo {self.edad} años')


# Instaciacion de objetos
persona01 = Persona('Pedro', 49, '0667896513')
persona02 = Persona('Cecilia', 44, '0655689651')

persona01.presentarse()
persona02.presentarse()
