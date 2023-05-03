def suma(*args):
    s = 0
    for i in args:
        s += i
    return s
resultado = suma(5,3,5,7,8,9)
print(resultado)