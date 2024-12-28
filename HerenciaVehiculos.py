import os
os.system('cls')

# Definir Superclase


class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def describir(self):
        print(f'Este vehículo es un {self.marca} {
              self.modelo} del año {self.año}.')

# Definir Subclases


class Coche(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def describir(self):
        super().describir()
        print(f'Tiene {self.puertas} puertas.')


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def describir(self):
        super().describir()
        print(f'Es una moto de tipo {self.tipo}.')


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def describir(self):
        super().describir()
        print(f'Es una bicicleta de tipo {self.tipo}.')


# Instanciar objetos
coche = Coche('Toyota', 'Corolla', 2020, 4)
moto = Moto('Yamaha', 'R1', 2021, 'Deportiva')
bicicleta = Bicicleta('Giant', 'Escape 3', 2019, 'Híbrida')

# Usar métodos de las instancias
coche.describir()
# moto.describir()
# bicicleta.describir()
