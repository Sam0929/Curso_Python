# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

novos_produtos = copy.deepcopy(produtos)

for element in novos_produtos:
    element['preco'] = round((element['preco'] * 1.10), 2)

#OU

novos_produtos = [
    {**p, 'preco': round((p['preco'] * 1.10), 2)} for p in produtos # ou for p in copy.deepcopy(produtos) # tem que prestar atencao se nao e necessario

]

print(*novos_produtos,'\n', sep = '\n')


produtos_ordenados_por_nome = sorted(produtos, key=lambda ord: ord['nome'], reverse = True)

print(*produtos_ordenados_por_nome,'\n', sep = '\n')


produtos_ordenados_por_preco = sorted(produtos, key=lambda ord: ord['preco'])

print(*produtos_ordenados_por_preco,'\n', sep = '\n')

print(*produtos,'\n', sep = '\n')