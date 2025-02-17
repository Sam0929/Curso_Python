"""
##Fatiamento de strings

 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: A funcao len retorna a quantidade 
de caracteres da string

"""

va = 'Olá Mundo'

print(va[4:])
print(va[4:7])
print(va[4:9])
print(va[-5:])
print(len(va[4:9]))
print(va[0:len(va)])
print(va[0:len(va):2]) #Pega um e pula outro
print(va[0:len(va):3]) #Pega um e pula dois
print(va[:-1])
print(va[::-1])
print(va[-1:-10:-1])



