# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
# print(lista)


lista = [
    numero
    for numero in range(10)
]
# print(lista)


# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco']* 1.1} for produto in produtos      #nova lista com aumento de preços
]

novos_produtos = [
    {**produto, 'preco': produto['preco']* 1.1}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos      #nova lista com aumento de preços se for maior que 20
]
print(*novos_produtos, sep = '\n')