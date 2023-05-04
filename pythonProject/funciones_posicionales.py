'''
def suma(*args):
    s = 0
    for i in args:
        s += i
    return s
resultado = suma(10,10,10,10)
print(resultado)
def lenguaje(nombre, *lenguajes):
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {lenguajes}')
lenguaje("Luis Calva","JAVA","Python","Php")
'''
def lenguaje(nombre,**lenguajes):
    print(f'Hola {nombre}')
    print("Buscando informacion acerca de tus lenguajes favoritos...")
    print("Cargando informacion ...\n")
    print("Informacion: ")
    contador = 0
    print(type(lenguajes))
    for clave in lenguajes:
        contador += 1
        print(f'Tu {contador} lenguaje favorito es: {lenguajes[clave]}')

lenguaje("Luis Calva",lenguaje1= "JAVA",lenguaje2 = "Python",lenguaje3 ="Php")