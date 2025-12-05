# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['a', 'b', 'c']]]]

def ordena (aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)     #para cada elemento do iterável:
grupos = groupby(alunos_agrupados, key=ordena)    #chave = key(elemento)
# grupos = groupby(sorted(alunos, key=lambda a: a['nota']), key = lambda a: a['nota'])


for chave, grupo in grupos:
    print(chave)
    print(list(grupo))

