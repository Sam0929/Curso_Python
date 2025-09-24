# Funcoes decoradaras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o python
# usar as funcoes decoradoras em outras funcoes
# Decoradores são syntax sugars



#para um codigo limpo, se voce tiver dificuldade em nomear uma funcao
#provavelmente ele deve ser dividia em mais de uma


def criar_funcao(func):                #funcao decoradora
    def interna(*args, **kwargs):
        print("ESTOU NO DECORADOR") 
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        resultado += ' = resultado'
        return resultado
    return interna


@criar_funcao #syntax sugar 
#@criar_funcao é uma abreviação para -> inverte_string = criar_funcao(inverte_string)
#ou seja, ao usar inverte_string, na verdade voce esta utilizando a 
#funcao que criar_funcao retornou e mandando os parametros para a funcao interna
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]



def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser string') 

# inverte_string_checando_parametro = criar_funcao(inverte_string)

# invertida = inverte_string_checando_parametro('67')

#NÃO É NECESSARIO USANDO SYNTAX SUGAR

invertida = inverte_string('123')

print(invertida)

# x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)