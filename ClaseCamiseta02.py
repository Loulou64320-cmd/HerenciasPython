import os

os.system('cls')

# Defino clase camiseta


class Camiseta:
    # Atributos de la clase
    def __init__(self, marca, precio, talla, color):
        self.marca = marca
        self.precio = precio
        self.talla = talla
        self.color = color

    # Metodo de la clase info de la clase
    def info_producto(self):
        info = f'Descripcion de la camiseta :\nMarca : {self.marca}\nPrecio : {
            self.precio}\nTalla : {self.talla}\nColor : {self.color}'
        return info


# Instanciamos el objeto camiseta
camiseta01 = Camiseta('Adidas', 25, 'M', 'Azul')
camiseta02 = Camiseta('Nike', 30, 'M', 'Rojo')

# Visualizacion del producto
print(camiseta01.info_producto())
print(camiseta02.info_producto())
