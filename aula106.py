
def create_decorators(a = None, b = None ,c = None): # Assim tenho acesso a 3 escopos #USO: OBTER PEGAR OS PARAMETROS DO DECORADOR

    def decorator(func): #USO: OBTER A FUNCAO

        print('Decoradora 1') # já é executado ao usar @decorator
        
        def inner(*args, **kwargs): #USO: FUNCAO ALVO SENDO EXECUTADA
            print('inner')
            res = func(*args, **kwargs)
            return res
        
        return inner

    return decorator


@create_decorators(1, 2, 3) #posso ter parâmetros aqui
def soma (x, y):
    return x + y

# decoradora = create_decorators()
# multiplica = decoradora(lambda x, y : x * y)

multiplica = create_decorators()(lambda x, y : x * y)

result = soma(10,10)
result_mult = multiplica(10 , 5)

print(result)
print(result_mult)



