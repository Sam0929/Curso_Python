#Introdução a formato

#Tudo em python são objetos, objetos que possuem métodos (ações que podem ser realizadas pelo objeto)

a = 'A'
b = 'B'
c = 1.1

string = 'a = {}, b = {}, c = {:.2f}'
string2 = 'a = {0}, a = {0}, a = {0}, b = {1}, c = {2:.2f}' # Usando índices
string3 = 'a = {nome1}, a = {nome1}, a = {nome1}, b = {nome2}, c = {nome3:.2f}' # Usando parâmetros

formato = string.format(a, b, c)
formato2 = string2.format(a, b, c)
formato3 = string3.format(nome1 = a, nome2 = b, nome3 = c)     #nome 3 é uma parâmetro c é um argumento


print(formato)
print(formato2)
print(formato3)