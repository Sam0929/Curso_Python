#try, except, else e finally

a = 18
b = 0
# b = (0,1)


try:
    c = a/b #NAO COLOCAR UMA EXCECAO E SILENCIAR UM ERRO, MA PRATICA

except (ZeroDivisionError, TypeError) as error: 
    print(f'MSG DE ERRO: {error = }')

try:
    c = a/b 
except (ZeroDivisionError, TypeError) as error: #error -> instancia da classe do erro
    print(f'MSG DE ERRO: {error}')
    print(f'NOME DO ERRO: {error.__class__.__name__}')