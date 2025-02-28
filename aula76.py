#Shallow Copy e Deep Copy

import copy

pessoa = {
    'nome': 'Samuel',
    'sobrenome': 'DSadad',
    'sei_la': [0, 1, 2],
    
}

pessoa2 = pessoa                   #não copia nada, só aponta para o mesmo endereço
print(f'Esse é o endereço de memória da pessoa 1:{id(pessoa)}, da pessoa 2:{id(pessoa2)}')

pessoa['nome'] = 'Blastoise'


print('\nEssa é a pessoa 1', pessoa)
print('Essa é a pessoa 2', pessoa2)  






pessoa2 = pessoa.copy()             #Shallow copy, copia tudo que é imutável para o outro dicionário, porém se houver dados mutáveis, não serão transferidos
print(f'\n\nEsse é o endereço de memória da pessoa 1:{id(pessoa)}, da pessoa 2:{id(pessoa2)}')


pessoa['nome'] = 'Samuel'


print('\nEssa é a pessoa 1', pessoa)
print('Essa é a pessoa 2', pessoa2)



pessoa['sei_la'][0] = 8888        #lista alterada em ambos os dicionários, pois é mutável

print(pessoa)
print(pessoa2)

pessoa2 = copy.deepcopy(pessoa)

pessoa['sei_la'][0] = 1221

print('USANDO DEEP COPY', pessoa)
print('USANDO DEEP COPY', pessoa2)

