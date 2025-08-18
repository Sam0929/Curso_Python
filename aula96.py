# raise - lancando excecoes (erros)
# # https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# def divide(n, d):
#     try:
#         return n / d
#     except ZeroDivisionError:
#         return "Deu Ruim"

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Divisor ZERO!!')
    return True

def only_int(x = None):
    if x is None:
        x = ()
    for num in x:
        if not isinstance(num, (int, float)):
            raise TypeError(f'{num} deve ser int ou float\n'
                            f'"{type(num).__name__}" foi enviado'
                            )
    return True
        
def divide(n, d):

    only_int((n,d))
    
    nao_aceito_zero(d)

    return n/d
    
print(divide(8, '1'))





# print(123)
# raise ValueError('Deu Erro')
#classe precisa ser executada ValueError somente nao basta, e
#necessario ValueError(), posso passar uma msg em ('Deu ruim')
# print(456)