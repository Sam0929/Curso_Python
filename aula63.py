def soma (x, y): #Parâmetros ficam na função

    soma = x / y
    return soma

#argumentos não nomeados

print(soma(1, 2)) #Argumentos são colocados na chamada da função

#argumentos nomeados, posso passar os parâmetros em qualquer ordem

print(soma(y = 2, x = 1))
