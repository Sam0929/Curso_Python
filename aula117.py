#funcoes recursivas
import sys

sys.setrecursionlimit(101)

def fatorial (n):
    if n == 1:
        return 1
    return n * fatorial(n-1)

print('\n====================================================')
print('Calculadora de fatorial com recursividade (Até 100)')
numero = int(input('Digite um número: '))

try:

    print (f'\nO fatorial de {numero} é:', fatorial(numero))

except(RecursionError) as error:

    print(f'\nVocê ultrapassou o limite máximo da recursão, erro: {error}')

