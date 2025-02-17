""" while/else """
string = 'Valor qualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break
 
    print(letra)
    i += 1
else:
    print('Não encontrei um espaço na string.')           # se houver alguma interrupção no while, antes do ciclo "normal" acabar ele não executa o else
print('Fora do while.')