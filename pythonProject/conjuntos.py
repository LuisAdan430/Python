'''
add // Añade un elemento al final del conjunto
clear // Elimina toda la informacion del conjunto
pop // Devuelve y elimina un elemento arbittrario o devuelve un error si esta vacio
remove // Intenta eliminar un elemento del conjunto, si no existe eleve un error
union // Devuelve un conjunto con todos los elementos de ambos conjuntos
'''
#Primera forma de crear conjuntos
alumnos = {"Andrea","Rubi","Marcos","Marlos","Jose"}
print(alumnos)
#Segunda forma de crear conjuntos
lenguajes = set(["Python","Java","Php","C"])
print(lenguajes)
#lenguajes.add("C#")
#lenguajes.clear()
#lenguajes.pop()
#lenguajes.remove("Java")
todos = alumnos.union(lenguajes)

print(todos)