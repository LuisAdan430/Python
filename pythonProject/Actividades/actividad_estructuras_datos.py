agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594
}
consultando = True
while consultando:
    print()
    print("MI AGENDA")
    print("------------------")
    print("1.Consultar \n2. Añadir \n3.Modificar \n4.Borrar \n5.Salir")
    opcion = ""
    while opcion not in ("1","2","3","4","5"):
        opcion = input("-> ")
        if opcion == "1":
            #Pedir nombre
            nombre = input("Nombre:  ")
            #Comprobar si el nombre esta en el diccionario
            if nombre not in agenda:
                print("Este nombre no existe en la agenda")
            else:
                telefono = agenda[nombre]
                print(nombre, ":", telefono )
        elif opcion == "2":
            #Pedir nombre
            nombre = input("Nombre: ")
            #Comprobar si el nombre esta en el diccionario
            if nombre in agenda:
                print("Este nombre ya esta en la agenda")
            else:
                telefono = int(input("Digite el telefono: "))
                #Añadir el telefono a la agenda
                agenda[nombre] = telefono
                print("El telefono se ha añadido correctamente")
        elif opcion == "3":
            #Pedir nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print("Este nombre no existe en la agenda")
            else:
                telefono = int(input("Digite el telefono: "))
                #Modificar el telefono
                agenda[nombre] = telefono
                print("El telefono se ha modificado correctamente")
        elif opcion == "4":
            #Pedir nombre
            nombre = input("Nombre: ")
            if nombre not in agenda:
                print("Este nombre no existe en la agenda")
            else:
                #Borrar el telefono
                del agenda[nombre]
                print("El telefono se ha borrado correctamente")
        elif opcion == "5":
            consultando = False
            print("Gracias por utilizar el programa")
