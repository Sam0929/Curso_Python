frase = 'aaaooo' 'asdfgasdgfag' 'asgrgrggrggrgrr'


i = 0
aux = None
width = len(frase)
print(width)


more_appears_count = 0
more_appears = None

while (i < width):

    aux = frase.count(frase[i])

    if(aux > more_appears_count):

        more_appears_count = aux
        more_appears = frase[i]
        
    i += 1

print(f'O caracter que mais aparece é "{more_appears}", esteve presente na frase um total de {more_appears_count} vezes')


