import sys

iterable = ['Eu','Tenho','__iter__']
iterator = iter(iterable)
#generator -> funcoes que sabem pausar #todo generator e um iterator, mas um iterator nao e um generator
lista = [n for n in range(1000)] #list comprehension #todos os dados ja estao na memoria
generator = (n for n in range(1000))  #isso e um generator
print(sys.getsizeof(lista))
print(len(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)
#generator economiza espaço quando nao se precisa ter todos os valores alocados na memoria