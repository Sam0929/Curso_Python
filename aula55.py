""" 
Imprecisão em ponto flutuante

O python utiliza a IEEE 754
Dobule-precision floating-point format IEEE 754

"""
import decimal

num_1 = decimal.Decimal('0.1')              #Se usada a função decimal, a precisão é corrigida
num_2 = decimal.Decimal('0.7')

num_3 = num_1 + num_2

print(num_3)

print(f'{num_3:.2f}')

print(round(num_3, 2)) # segundo argumento é o numero de casas decimais

