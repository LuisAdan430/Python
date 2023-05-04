'''
Crear una tupla con numeros, luego pedir un numero por teclado e indicar
'''
numero = (5,6,7,8,5,5,6,90,12,14,12)
numeros = int(input("Dame un numero: "))
#print("El numero se repite : ", str(numero.count(numeros))+ "veces")
print("El numero " +str(numero) + "se encuentra en el indice: " + str(numero.index(numeros)))