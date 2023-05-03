'''
word = input("Ingresa una palabra: ")
for iterar in range(10):
    print(word)
'''
'''
print('Comienzo')
contador = 1
for i in[3,4,5,7,8]:
    print(f'Vuelta numero: {contador}')
    print(f'Hola,ahora i vale {i} y su cuadrado es {i ** 2}')
    contador += 1
print('Final')
'''
numero = int(input("¿De que numero quieres la tabla de multiplicar?"))
print("")
print(f'Tabla  de multiplicar del numero{numero}')
for i in range(1,11):
    print(f'{i} x {numero} = {i*numero}')