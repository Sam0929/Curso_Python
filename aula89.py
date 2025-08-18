#iteráveis tem sequência
#iteradores te entregar um valor por vez, não importando a sequência

iterable = ['Eu','Tenho','__iter__']
iterator = iterable.__iter__()
print(next(iterator)) #a unica coisa que o iterator sabe