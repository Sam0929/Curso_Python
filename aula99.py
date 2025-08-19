import importlib

import aula99_m

print(aula99_m.variavel)

for i in range(10):
    print(i)
    importlib.reload(aula99_m)  #recarrega o import, usar se necessario
    #import aula99_m #nao recarrega o modulo

print('Fim')