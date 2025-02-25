
#funções com parâmetros com valores padrões
#caso o valor não seja enviado, o valor padrão será usado

def soma(x, y, z=None):
    if z is not None:
        print(x+y+z)
    else:
        print(x+y)

soma(10, 20)

