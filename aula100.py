#packages em python
from sys import path

import aula100_package #nao faz nada

from aula100_package.modulo import soma
#ou
import aula100_package.modulo as a
#ou
from aula100_package import modulo

#ma pratica, mas somente para exemplificar o dunder all
from aula100_package.modulo import *
print(x)

print(a.soma(2,4))

print(modulo.soma(2,4))

print(soma(2,4))

# print(*path, sep='\n')
# print(__name__)


from aula100_package.modulo2 import qualquer_coisa

qualquer_coisa()