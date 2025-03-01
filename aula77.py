# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)

last_key = p1.popitem()
print(last_key)
print(p1)

# p1.update({
#      'nome': 'new value',
#      'age' : 30


# })


#OR


# p1.update(nome='novo valor', age = 30)


#OR


tupla = (('nome', 'novo valor'), ('age', 30))
lista = [['nome', 'novo valor'], ['age', 30]]
p1.update(lista)                                      # update pode receber um iterável que contém outro iterável com chave e valor, ou seja, pode receber um iterável que se comporta como um dicionário

print(p1)