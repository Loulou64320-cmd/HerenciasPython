import os
os.system('cls')


# Definir Superclase
class Animal():
    def __init__(self, nombre, edad, especie, color):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.color = color

    def describir(self):
        """print("{} es un(a) {} de color {}".format(self.nombre, self.especie, self.color))"""
        print(f'{self.nombre} es un(a) {self.especie} de color {self.color}')


# Definir Subclases
class AnimalAereo(Animal):
    """def __init__(self, nombre, edad, especie, color):
        super().__init__(nombre, edad, especie, color)"""

    def volar(self):
        print(f'{self.nombre} es un(a) {self.especie} puede volar')


class AnimalTerrestre(Animal):
    def caminar(self):
        print(f'{self.nombre} es un(a) {self.especie} puede correr')


class AnimalAcuatico(Animal):
    def nadar(self):
        print(f'{self.nombre} es un(a) {self.especie} puede nadar')


# Instanciar objeto
elefante = AnimalTerrestre('Juana', 50, 'Elefante', 'gris')
aguila = AnimalAereo('Real', 2, 'Aguila', 'blanco')
pez_rojo = AnimalAcuatico('Nemo', 1, 'Pez rojo', 'rojo')

elefante.describir()
aguila.describir()
pez_rojo.describir()

elefante.caminar()
aguila.volar()
pez_rojo.nadar()
