'''HIGH ORDER FUNCTIONS'''


def hello(msg, nome):
    return f'{msg}, {nome}!'

def execute(func, *args):          #  *  empacota em uma tupla
    return func(*args)             #  * desempacota



v = execute(hello, 'Hello', 'Samuel')
print(v)