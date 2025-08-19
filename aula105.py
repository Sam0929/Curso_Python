# Funcoes decoradaras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funcoes decoradoras sao funcoes que decoram outras funcoes
# Decoradores sao usados para fazer o python
# usar as funcoes decoradoras em outras funcoes



#para um codigo limpo, se voce tiver dificuldade em nomear uma funcao
#provavelmente ele deve ser dividia em mais de uma


def criar_funcao(func):                #funcao decoradora
    def interna(*args, **kwargs): 
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        return resultado
    return interna

def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Parametro deve ser string') 

inverte_string_checando_parametro = criar_funcao(inverte_string)

invertida = inverte_string_checando_parametro('67')

print(invertida)

# x, y, *resto = 1, 2, 3, 4

# print(x, y, resto)