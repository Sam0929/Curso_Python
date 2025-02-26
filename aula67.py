#*args (empacotamento e desempacotamento)


def soma (x, y):
    return x + y

soma(1,2)

def soma_args(*args):

    total = 0
    
    for num in args:
        total += num

    return total

print(soma_args(1, 10, 20, 333, 44))


