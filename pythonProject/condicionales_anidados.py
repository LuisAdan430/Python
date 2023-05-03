'''

edad = int(input("¿Cuantos años tienes ?"))
graduacion = str(input("¿Ya te has graduado? (si) o (no) ?"))
if edad > 18:
    print("Felicidades! Ya tienes la mayoria de edad")
    if graduacion == 'si':
        print("Felicidades por tu graduacion!")
'''
password = input("Ingresa la contraseña: ")
if(len(password) >= 8):
    print("Muy bien, contraseña suficientemente larga")

    if(password == 'Prueba12345'):
        print("Ademas, es a contraseña correcta")
    else: print("Pero es incorrecta")
else:
    print("Tu contraseña es muy corta e insegura")
    print("Ademas, es incorrecta")