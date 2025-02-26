#Outra forma
# 
# 
# #*args (empacotamento e desempacotamento) o * nos parâmetros diz para a função que todos os argumentos que ela receber serão empacotados em uma tupla


def soma (x, y):
    return x + y

soma(1,2)

def soma_args(*args):

    total = 0
    
    for num in args:
        total += num

    return total

print(soma_args(1, 10, 20, 333, 44))

# sum pode ser usado

print(sum((1, 10, 20, 333, 44))) # observe que um iterável deve ser passado como argumento