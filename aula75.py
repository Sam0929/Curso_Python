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


pessoa = {
    'nome': 'Samuel',
    'sobrenome': 'DSadad',
    
}

print(pessoa.__len__())
#ao inver disso usar
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())

pessoa.setdefault('idade', 0) #se o campo idade não existir, o padrão será 0 ou None se 0 não for passado

print(pessoa['idade'])    #exemplo


for chave, valor in pessoa.items():
    print(chave, valor)
