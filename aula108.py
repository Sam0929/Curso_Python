Cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
Estados = ['BA', 'SP', 'MG', 'RJ']

print(len(Cidades))
print(len(Estados))


def decorator(func):
    def inner(*args):
        if (len(args[0]) > len(args[1])):
            res = func(*args)
        return res
    return inner

@decorator
def unir_d0(data0, data1):
    return


