import os
os.system('cls')


# Definir Superclase
class Animal():
    def __init__(self, nombre, edad, especie, color):
        self.nombre = None
        self.edad = None
        self.especie = None
        self.color = None

    def describir(self):
        """print("{} es un(a) {} de color {}".format(self.nombre, self.especie, self.color))"""
        os.system('cls')
        print(f'\n\t{self.nombre} es un(a) {
              self.especie} de color {self.color}')

    def nombre_animal(self, nombre):
        self.nombre = nombre

    def edad_animal(self, edad):
        self.edad = edad

    def especie_animal(self, especie):
        self.especie = especie

    def color_animal(self, color):
        self.color = color


# Definir Subclases
class AnimalAereo(Animal):
    def volar(self):
        print(f'\t\t{self.nombre} es un(a) {self.especie} que puede volar')


class AnimalTerrestre(Animal):
    def caminar(self):
        print(f'\t\t{self.nombre} es un(a) {self.especie} que puede correr')


class AnimalAcuatico(Animal):
    def nadar(self):
        print(f'\t\t{self.nombre} es un(a) {self.especie} que puede nadar')


# Datos del animal
nombre_del_animal = input('\tDale un nombre a tu animal: ')
edad_del_animal = input('\tDale una edad a tu animal: ')
especie_del_animal = input('\tDale una especie a tu animal: ')
color_del_animal = input('\tPonle un color a tu animal: ')

# Instanciar animal
instacia_animal = AnimalTerrestre(None, None, None, None)

# Asignar los datos del animal a la instancia animal
instacia_animal.nombre_animal(nombre_del_animal)
instacia_animal.edad_animal(edad_del_animal)
instacia_animal.especie_animal(especie_del_animal)
instacia_animal.color_animal(color_del_animal)

# Presentar animal
instacia_animal.describir()

instacia_animal.caminar()
