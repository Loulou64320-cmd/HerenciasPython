import os
os.system('cls')

# Clase


class Automovil():
    # Atributos de la clase
    def __init__(self, marca, modelo, ano, color):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

    # Metodos de la clase
    def info_automovil(self):
        info = f'Descripcion :\nSoy un auto\nnmarca: {self.marca}\nmodelo: {
            self.modelo}\naño: {self.ano}'
        print("------------")
        return info


# Instanciar objetos
automovil01 = Automovil('Chevrolet', 'Aveo', 2012, 'gris')
automovil02 = Automovil('Ford', 'Ecosport', 2020, 'rojo')

print(automovil01.info_automovil())
print(automovil02.info_automovil())
