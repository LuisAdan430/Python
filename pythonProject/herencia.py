class Vehiculo():
    def __init__(self,matricula,modelo,marca,color):
        self.matricula = matricula
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.avanza = False
        self.frena = False
        self.gira = False
    def avanzar(self):
        self.avanza = True
    def frenar(self):
        self.frena = True
    def girar(self):
        self.gira = True
    def imprimir(self):
        print(f'Marca: {self.matricula} \n Modelo: {self.modelo} \n Marca: {self.marca} \n'
              f'Color: {self.color} \n Avanzar: {self.avanza} \n Frenar:{self.frena} \n'
              f'Girar: {self.gira} ')


class Moto(Vehiculo):
    def __init__(self,matricula,modelo,marca,color,cilindraje):
        super().__init__(matricula,modelo,marca,color)
        self.cilindraje = cilindraje

moto1 = Moto("ABC123",2019,"BMW","Rojo",150 )
moto1.avanzar()
moto1.girar()
moto1.frenar()
print("Cilindraje " + str(moto1.cilindraje))
moto1.imprimir()