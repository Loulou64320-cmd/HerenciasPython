import os
os.system('cls')


# Definir Superclase
class Animal():
    def __init__(self, nombre, edad, especie, color):
        self.nombre = None
        self.edad = edad
        self.especie = None
        self.color = color

    def describir(self):
        """print("{} es un(a) {} de color {}".format(self.nombre, self.especie, self.color))"""
        print(f'{self.nombre} es un(a) {self.especie} de color {self.color}')

    def nombre_animal(self, nombre):
        self.nombre = nombre

    def especie_animal(self, especie):
        self.especie = especie


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


# Datos del animal
nombre_del_animal = input('Dale un nombre a tu animal: ')
especie_del_animal = input('Dale una especie a tu animal: ')

# Instanciar animal
instacia_animal = Animal(None, 5, None, 'negro')

# Asignar los datos del animal a la instancia animal
instacia_animal.nombre_animal(nombre_del_animal)
instacia_animal.especie_animal(especie_del_animal)

# Presentar animal
instacia_animal.describir()
