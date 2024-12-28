import os

os.system('cls')


class MiPerrito:
    # Constructor
    def __init__(self, nombre, edad, raza, sexo, color):
        self.nombre = None
        self.edad = edad
        self.raza = raza
        self.sexo = sexo
        self.color = color

    # Metodos

    def ladrar(self):
        print(f'{self.nombre} esta ladrando ')

    def comer(self):
        print(f'{self.nombre} esta comiendo ')

    def jugar(self):
        print(f'{self.nombre} esta jugando')

    def nombrar_perro(self, nombre):
        self.nombre = nombre
        print(f'El perro se llama {nombre}')


# Instanciar un objeto
mi_perro = MiPerrito(None, 5, 'Pitbull', 'Hembra', 'Atigrada')
# Asignar el nombre
mi_perro.nombrar_perro('Christa')

mi_perro.ladrar()
mi_perro.comer()
mi_perro.jugar()
