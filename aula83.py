
# def soma(x, y):
#     return x + y


# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica


def execute(function, *args):
    return function(*args)

print(execute(lambda x, y: x + y, 321, 33))

mult_5 = execute(lambda multiplier: lambda num: num * multiplier, 5)

print(mult_5(30))


print(execute(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9))