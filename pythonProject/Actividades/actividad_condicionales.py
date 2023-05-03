#Descuentos
nombre = str(input("Ingrese su nombre: "))
compra_valor = float(input("Ingrese  el valor de la compra sin descuento: "))
valor_final= 0.0
descuento = 0.0
if(compra_valor < 80):
    valor_final = compra_valor
    print("Esta compra no contiene descuento")
    print(f'El valor final es : {float(valor_final)}')
elif(compra_valor >= 80 and compra_valor <150 ):
    descuento = compra_valor * 0.10
    valor_final = compra_valor - descuento
    print("Esta compra contiene un descuento del 10%")
    print(f'El valor final es : {float(valor_final)}')