from itertools import zip_longest


Cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
Estados = ['BA', 'SP', 'MG', 'RJ']

def zipper(l1, l2):
    intervalo = min (len(Cidades), len(Estados))
    return [(Cidades[i], Estados[i]) for i in range(intervalo)]


print(zipper(Cidades, Estados))

print(list(zip(Cidades, Estados)))
print(list(zip_longest(Cidades, Estados, fillvalue= 'Sem cidade')))