a, b = 1, 2
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Alves'
}

dados_pessoa = {

    'idade' : 16,
    'altura' : 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)


(a, b), (c, d) = pessoa.items()
print(pessoa.keys())

print(a, b, c, d)


# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def testing_kw_args(**kwargs):
    print(kwargs)
    
testing_kw_args(xddd = 12312)
testing_kw_args(**pessoa_completa)
