# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import sys

from aula98_m import soma

print("Este modulo se chama", __name__)
print(soma(2,4))
print(*sys.path, sep='\n')

# sys.path.append('/home')
#pastas no python sao chamadas de pacotes, quando se tem modulos dentro delas


#para ter um codigo limpo, uma boa pratica e ter todos os modulos juntos com o main, no mesmo diretorio, pode ser em outras pasta, mas para dentro, nunca para fora