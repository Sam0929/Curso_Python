"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe o escopo global e o local
O escopo global é o escopo onde todo o código é ancançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos 
externos.
Temos acesso a nomes de escopos externos nos escopos internos
A palavra global faz uma variável do escopo externo
ser a mesma no escopo interno.

"""


# def escopo():
#     x = 1
#     print(x)

# # print(x) Não definido

# escopo()


x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)