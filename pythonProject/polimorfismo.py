class Gato():
    def sonido(self):
        print("MIAU")
class Perro():
    def sonido(self):
        print("GUAU")
class Cerdo():
    def sonido(self):
        print("OING OING")
def escucharSonido(animal):
    animal.sonido()
gato1 = Gato()
perro1 = Perro()
cerdo1 = Cerdo()
escucharSonido(cerdo1)
