#manipulando chaves e valores em dicionários

pessoa = {}
 
pessoa['nome'] = 'Samuel Vfa'        #criacao dinamica
pessoa['sobrenome'] = 'SSA'




print(pessoa['nome'])                    #read

pessoa['nome'] = 'Samuel Blabla'          # update

print(pessoa)                       


del pessoa['sobrenome']                     #delete

print(pessoa)



if pessoa.get('sobrenome') is not None:
    print(pessoa['sobrenome'])
else:
    print('Sobrenome não existe')



if pessoa.get('sobrenome', False):
    print(pessoa['sobrenome'])
else:
    print('Sobrenome não existe')
