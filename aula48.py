'''
Listas em Python
Tipo list - Mútavel
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append- , insert -, pop, del, clear, extend, + 

#........+01234
#........-54321


'''

# array = ['João', 'Maria', 10, 123.44, True, [] ]
# print(array, type(array))

# #print(bool([]))    # falsy
# print(array [2:6:3])
# array[0] = 'Luiz'
# print(array)


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)

# string = 'nome'
# print(string)
# string = 'laa'
# print(string)

# string[0] = 'a' # imutável

# i = 0
# tamanho_lista = 10000
# array = list(range(tamanho_lista))

# for i in range(0, len(array), 1000):  # Imprime de 1000 em 1000 números
#     print(array[i:i+1000])


"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Luiz')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
print(lista)
lista.insert(2, 5)  # índice e valor
print(lista)




lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_d = lista_a.extend(lista_b)   #método extend não retorna nada, mas altera a primeira lista
print('Lista_d atribuindo com extend (n funciona)', lista_d) 
print(lista_a)
lista_d = lista_a + lista_b
print('Lista D com +', lista_d)