'''
#Primera forma de crear un diccionario
diccionario = {
    "Nombre": "Luis",
    "Edad": 28,
    "Documento": 456234
}
print(diccionario)
#Segunda forma de crear un diccionario
diccionario_segunda_forma = dict(Nombre = 'Adan',Edad= 37,Documento= 54445)
print(diccionario_segunda_forma)

#Tercera forma de crear un diccionario
diccionario_tercera_forma = dict([
    ('Nommbre','Angel'),
    ('Edad', 26),
    ('Documento',5467)
])
print(diccionario_tercera_forma)
'''
inventario = {"Manzanas":235,"Peras":400,"Naranjas":250,"Sandias":500}
#inventario.keys()
#inventario.values()
print(inventario.items())