'''

Enumerate - enumera iteráveis (índices)

'''

array = ['Maria', 'José', 'Helena', 'Samuel']


lista_enumerada = enumerate(array) # gera um objeto enumerado

print(lista_enumerada)

for nome in lista_enumerada:
    print(nome)


for nome in enumerate(array):
    print(nome)
for nome in enumerate(array):
    print(nome)
for nome in enumerate(array):
    print(nome)
    
lista_enumerada = list(enumerate(array))
lista_enumerada = list(enumerate(array, start = 1))

print(lista_enumerada)

for nome in enumerate(array):   #enumerate gera uma tupla pra cada elemento, com dois valores, é possível usar o desempacotamento para separar
    indice, name = nome
    print(indice, name)

# ou

for indice, nome in enumerate(array):
    print(indice, nome)


for tupla in enumerate(array): # \t é um tab em strings
    print('FOR da tupla:') 
    for valor in tupla: 
        print(f'\t{valor}')