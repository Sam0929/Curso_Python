# variaveis livres + nonlocal (locals + globals)
# toda global pode ser livre, mas nem toda livre e global, uma livre pode ser de uma funcao 'pai'
def fora(x):
    a = x   
    # print(*globals(), sep = '\n')
    def dentro():
        # print(locals())
        print(dentro.__code__.co_freevars)
        return a #a e variavel livre no escopo de dentro()
    return dentro

dentro = fora(10)
dentro2 = fora(20)

print(dentro())
print(dentro2())



def concatenar(string_inicial):
    valor_final = string_inicial
    def interna(valor):
        nonlocal valor_final
        valor_final += valor #nao e possivel sem nonlocal, pois e uma variavel livre e deve ser buscada no escopo acima
        return valor_final #free var
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(c('e'))