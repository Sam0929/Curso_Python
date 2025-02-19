"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()  #dessa forma são duas lista independentes, mudar um valor na b não altera na a
# lista_b = lista_a # aponta para o mesmo id, ou seja, é a mesma lista, alterar qualquer uma das duas variaveis altera a mesma lista

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


name = 'Luiz' 
xpto = name     # = - copiado o valor (imutáveis)
print(name)
xpto = 'Jorge'
print(xpto)
print(name)