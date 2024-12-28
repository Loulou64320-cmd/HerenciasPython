import os
os.system('cls')

# Define Superclase o clase padre


class Animal:
    # Atributos
    def __init__(self, nombre, especie, color):
        self.nombre = nombre
        self.especie = especie
        self.color = color

    # Metodos
    def describir(self):
        print(f'{self.nombre} es un(a) {self.especie} de color {self.color}')

    def hacer_sonido(self, sonido):
        print(f'{self.nombre} hace "{sonido}".')


# Definir subclases
class AnimalAereo(Animal):
    # Atributos de la subclase
    def __init__(self, nombre, especie, color, altitud_maxima_vuelo):
        super().__init__(nombre, especie, color)
        self.altitud_maxima_vuelo = altitud_maxima_vuelo

    # Metodos de la subclase
    def volar(self):
        print(f'{self.nombre} puede volar hasta una altura de {
              self.altitud_maxima_vuelo} m')


class AnimalTerrestre(Animal):
    # Atributos de la subclase
    def __init__(self, nombre, especie, color, velocidad_maxima):
        super().__init__(nombre, especie, color)
        self.velocidad_maxima = velocidad_maxima

    # Metodos de la subclase
    def correr(self):
        print(f'{self.nombre} puede correr a una velocidad maxima de {
              self.velocidad_maxima} Km*h')


class AnimalAcuatico(Animal):
    def __init__(self, nombre, especie, color, profundidad_maxima):
        super().__init__(nombre, especie, color)
        self.profundidad_maxima = profundidad_maxima

    def nadar(self):
        print(f'{self.nombre} puede nadar hasta una profundidad de {
              self.profundidad_maxima} m')


# Instanciar objetos
aguila = AnimalAereo('Aguila Real', 'Aguila', 'Marron', 3000)
guepardo = AnimalTerrestre('Chitara', 'Guepardo', 'Marron con manchas', 100)
delfin = AnimalAcuatico('Flipper', 'Delfin', 'Gris', 300)


aguila.describir()
aguila.hacer_sonido('chillido')
aguila.volar()

guepardo.describir()
guepardo.hacer_sonido('gruñidos')
guepardo.correr()

delfin.describir()
delfin.hacer_sonido('clics')
delfin.nadar()
