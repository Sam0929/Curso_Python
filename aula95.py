#try, except, else e finally

try:
    print(1)
    #open(arquivo)
    # a = 8/0
except ZeroDivisionError:
    print("dividiu zero")
else:
    print('Nao ocorreu erro')
finally: #sempre sera executado, apos o try, mesmo que ocorra um erro
    print(2)
    #fechar(arquivo) #Independente da excecao, seria interessante fechar o arquivo