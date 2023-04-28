edad = int(input("¿Cuantos años tienes ?"))
graduacion = str(input("¿Ya te has graduado? (si) o (no) ?"))
if edad > 18:
    print("Felicidades! Ya tienes la mayoria de edad")
    if graduacion == 'si':
        print("Felicidades por tu graduacion!")