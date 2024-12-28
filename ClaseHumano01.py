import os

os.system('cls')


class Humano:
    # Atributos
    def __init__(self, nombre, edad, anhelo):
        self.nombre = nombre
        self.edad = edad
        self.anhelo = anhelo

    # Metodo
    def presentarse(self):
        presentacion = f'¡Hola! soy {self.nombre} tengo {
            self.edad} años y me gustaria ser {self.anhelo}'
        print('--------')
        return presentacion


# Instancio objeto
humano01 = Humano('Pedro', 49, 'Programador de Sistemas')
humano02 = Humano('Cecilia', 44, 'Jefa de Aduanas')
humano03 = Humano('Joram', 19, 'Electricista indrustrial')

# Presenta en consola
print(humano01.presentarse())
print(humano02.presentarse())
print(humano03.presentarse())
