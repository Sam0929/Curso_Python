"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

if (len(lista_a) < len(lista_b)):
    menor = lista_a
else:
    menor = lista_b

lista_soma = []

for i in range (len(menor)):
    soma = lista_a[i] + lista_b[i]
    lista_soma.append(soma)

print('Minha solução ruts: ', lista_soma)

lista_soma = [x + y for x, y in zip(lista_a, lista_b)]

print('Solução mais limpa:', lista_soma)