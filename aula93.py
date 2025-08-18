#try, except, else e finally

a = 18
b = 0
b = (0,1)


try:
    c = a/b #NAO COLOCAR UMA EXCECAO E SILENCIAR UM ERRO, MA PRATICA

except ZeroDivisionError: #dessa forma somente o erro esperado e tratado
    print('Dividiu por zero') #tratamento inadequado se nao tiver a classe, qualquer erro vai ser dividiu por zero
except NameError:
    print('Algo nao esta definido') 
except Exception:
    print('Erro desconhecido')
except (TypeError, IndexError, IndentationError):
    print('Type + Index + Identation')    
print('CONTINUAR')