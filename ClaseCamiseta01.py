import os

os.system('cls')

# Creamos una clase


class Camiseta:
    # Inicializamos con Init
    def __init__(self, marca, precio, talla, color):
        # Creamos Atributos
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color


# instanciamos un objeto nuevo

camiseta01 = Camiseta('nike', 20, 'M', 'negro')
camiseta02 = Camiseta('adidas', 30, 'L', 'blanco')
camiseta03 = Camiseta('polo', 25, 'S', 'celeste')
camiseta04 = Camiseta('gucci', 35, 'XL', 'rojo')

# Acceder al atributo de cada instancia creada

print(camiseta01.marca)
print(camiseta02.precio)
print(camiseta03.talla)
print(camiseta04.color)
