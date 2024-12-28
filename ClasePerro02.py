import os

os.system('cls')


class MiPerrito:
    # Constructor
    def __init__(self, nombre, edad, raza, sexo, color):
        self.nombre = None
        self.edad = None
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

    def edad_perro(self, edad):
        self.edad = int(edad)
        print(f'El perro tiene {edad} años')

    def presentacion(self):
        if self.edad < 2:
            presentacion = print(f'¡Hola! mi perro se llama {self.nombre} es un {
                                 self.raza} tiene {self.edad} año y es de color {self.color}')
        else:
            presentacion = print(f'¡Hola! mi perro se llama {self.nombre} es un {
                                 self.raza} tiene {self.edad} años y es de color {self.color}')


# Pedir datos del perro
nombre_del_perro = input('Ingrese el nombre del perro: ')
edad_del_perro = input('Ingrese la edad: ')

# Instanciar un objeto
mi_perro = MiPerrito(None, None, 'Pitbull', 'Hembra', 'Atigrada')

# Asignar el nombre ingresado por el usuario
mi_perro.nombrar_perro(nombre_del_perro)
mi_perro.edad_perro(edad_del_perro)

# Presentar al perro
mi_perro.presentacion()

mi_perro.ladrar()
mi_perro.comer()
mi_perro.jugar()
