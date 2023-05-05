class Persona:
    def __init__(self,identificacion,nombre,edad):
        self.__identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
    def saludo(self):
        return "Hola " + self.nombre
    def getIdentificacion(self):
        return self.__identificacion
    def setIdentificacion(self,valor):
        self.__identificacion = valor

persona1 = Persona(456789,"Adan",25)

#print(persona1._Persona__identificacion)
persona1.setIdentificacion(26)
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)
