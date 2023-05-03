'''
def es_par(numero):
    if numero % 2 == 0:
        print(f'El numero {numero} es par')
    else:
        print(f'El numero {numero} es impar')
es_par(5)

def saludar(nombre):
    print("Hola " +nombre +" Eres el mejor programdor")

saludar("marcos")

def resta ( a= None, b = None):
    if a == None or b == None:
        print("Error,debes enviar dos numeros a la funcion")
        return
    return a-b
resultado = resta(5,2)
print(resultado)
'''
def multiplicacion(numero = None):
    if numero == None:
        print("Por favor,introduce un numero")
    else:
        print(f'Tabla de multipicar del {numero}')
        for i in range(1,11):
            print(f'{i} x {numero} = {i * numero}')

multiplicacion(4)

