'''
Tipo tupla - Uma lista imútavel

'''

nomes = 'Samuel', 'Maria', 'José' # tupla
print(nomes)
nomes2 = 'Samuel', 'Maria', 'José'
nomes2 = nomes.__add__(nomes2) # == nomes + nomes2
print(nomes2)

nomes2 = list(nomes2)

print(nomes2, type(nomes2))

nomes2.sort()

print(nomes2)