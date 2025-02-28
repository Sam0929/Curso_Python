'''
Closure e funções que retornam outras funções

'''


def hello(msg):
    def say(name):
        return f'{msg}, {name}!!'
    return say

say_good_morning = hello('Good morning')
say_good_afternoon = hello('Good afternoon')
say_good_night = hello('Good night')


print(say_good_morning('Samuel')) # -> Closure, valores da função salvos
print(say_good_afternoon('Samuel')) # -> Closure, valores da função salvos
print(say_good_night('Samuel')) # -> Closure, valores da função salvos

for nome in ['Samuel', 'Luiz', 'John', 'Maria', 'Jorge']:
    print(say_good_morning(nome))
    print(say_good_afternoon(nome))
    print(say_good_night(nome))