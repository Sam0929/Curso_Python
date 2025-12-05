# partial e map

from functools import partial

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    porcentagem = porcentagem/100
    return round(valor + valor * porcentagem, 2)  

aumentar_dez_porcento = partial(        # partial retorna uma nova funcao com um parametro pre definido
    aumentar_porcentagem,
    porcentagem = 10
)

def altera_valor(produto):
   return {
       **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
        } 
  
novos_produtos = [
    {**p, 'preco': aumentar_porcentagem(p['preco'], 20)} for p in produtos
]

novos_produtos_10 = [
    {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
]

novos_produtos_map = map(
    altera_valor,
    produtos
)
# print(novos_produtos)

# print(novos_produtos_10)

print(novos_produtos_map)
print_iter(novos_produtos_map)

print(
    list(
        map(
            lambda x: x * 3,
            [1, 3, 6, 9]
        )
    )
)