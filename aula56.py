"""

split e join com list e str
split - divide uma string
join - une uma string

"""

frase = "Olha só que legal, coisa interessante!"
lista_palavras0 = frase.split()
lista_palavras1 = ' '.join(map(str, frase.split()))
print(frase)
print (lista_palavras0)
print(lista_palavras1)

lista_por_virgula = frase.split(',')

print(lista_por_virgula)

lista_corrigida = []

for word in lista_por_virgula:

    lista_corrigida.append(word.strip())

    print(word.lstrip())

print(lista_corrigida)


frases_unidas = ' '.join(['abc', 'ab'])  # posso fazer um join com tudo que é iterável, listas, tuplas, etc
print(frases_unidas) #join coloca a string que chamou o método entre cada elemento 

