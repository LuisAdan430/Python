'''
primer ejemplos:
crear un programa que reciba el numero de años que tiene nuestra computadora
Imprimir en consola si es nuevo o es viejo
Condiciones: Si es menor o mayor a dos años,entonces es nuevo.
Pero es mayor a 2 años entonces es viejo
'''
'''
anios = int(input("Cuantos años tiene tu computador?"))
if anios >= 0 and anios <= 2:
    print("Tu computador es nuevo")
else:
    print("Tu computador es viejo")
'''
edad = int(input("¿Cuantos años tienes?"))
if edad >= 18:
    print("Es usted mayor de edad")
else:
    print("Es usted menor de edad")
print("¡Hasta la proxima!")