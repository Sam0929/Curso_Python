'''

Introdução ao desempacotamento + tuples (tuplas)


'''


array = ['Maria', 'José', 'Helena', 'Samuel']

#Como desempacotar?

nome1, nome2, nome3, nome4 = array

nome1, *resto = array  #desempacota o primeiro valor da lista e coloca o resto em resto

print(nome1)

print(resto)

_, nome12, *resto = array

print(array)

print(nome12)