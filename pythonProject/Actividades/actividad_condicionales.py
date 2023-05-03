#Descuentos
nombre = str(input("Ingrese su nombre: "))
valor_compra = float(input("Ingrese  el valor de la compra: "))
precio_final= 0.0
descuento = 0.0
if(valor_compra < 80):
    precio_final = valor_compra
    print("Esta compra no contiene descuento")
    print(f'Hola, {nombre}. El valor a pagar es : $ {float(precio_final)}')
elif(valor_compra >= 80 and valor_compra <150 ):
    descuento = valor_compra * 0.10
    precio_final = valor_compra - descuento
    print("Esta compra contiene un descuento del 10%")
    print(f'Hola, {nombre}. El valor a pagar es : $ {float(precio_final)}')
elif(valor_compra >= 150 and valor_compra <= 300):
    descuento = valor_compra * 0.15
    precio_final = valor_compra - descuento
    print("Esta compra contiene un descuento del 15%")
    print(f'Hola, {nombre}. El valor a pagar es : $ {float(precio_final)}')
elif(valor_compra > 300 and valor_compra < 500):
    descuento = valor_compra * 0.20
    valor_final = valor_compra - descuento
    print("Esta compra contiene un descuento del 20%")
    print(f'Hola, {nombre}. El valor a pagar es : $ {float(valor_final)}')

    '''
    Angel Mario Villa Lopez realizo una compra de 445usd : 
        Hola, Angel Mario Villa Lopez. El valor a pagar es : $ 356.0
    Rosa Diaz realizo una compra de 105usd:
        Hola, Rosa Diaz. El valor a pagar es : $ 94.5
    Dilan Gonzales realizo una compra de 250usd :
        Hola, Dilan Gonzales. El valor a pagar es : $ 212.5
    Kelly Daza realizo una compra de 430usd: 
        Hola, Kelly Daza. El valor a pagar es : $ 344.0
    
    '''