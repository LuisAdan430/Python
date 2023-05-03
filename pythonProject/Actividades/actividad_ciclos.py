#Mi promedio Universitario
nombre_estudiante = input("Ingrese su nombre :")
numero_materias = int(input("Ingrese el numero de materias que curso: "))
contador = 1
sumatoria = 0
while contador <= numero_materias:
     nombre_materia = input("Ingresa el nombre de la (" +str(contador) + ") materia: ")
     calificacion = float (input ("calificacion obtenidas en" + str(nombre_materia) + ": "))
     sumatoria = sumatoria + calificacion
     contador = contador + 1
     promedio = sumatoria / numero_materias
print("***RESULTADOS***")
print(f' Hola , {nombre_estudiante} tienes un promedio de {promedio} en el 5to Semestre.')

# ¿Cuál es tu nombre y qué promedio obtuviste?
#***RESULTADOS***
#Hola , Luis tienes un promedio de 8.6 en el 5to Semestre.

