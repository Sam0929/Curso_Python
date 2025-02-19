import os

"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.

"""

def Apagar(lista):

    if not lista:

        print("A lista esta vazia!!")

        input("Aperte qualquer tecla para continuar....")
        
        return

    Listar(lista, 1)

    while True:

            try: 

                i = int(input('\nDigite um índice:'))


                del lista[i]

                print("Valor deletado com sucesso!!")

                break

             
            except ValueError:           # É uma boa prática especificar o erro para que outros erros genéricos não sejam mascarados

                print("Você não digitou um índice, por favor tente novamente!!")

            except IndexError:

                print("Índice não existente")

            except Exception:
                
                print("Erro desconhecido!!")
    
    input("Aperte qualquer tecla para continuar....")

def Inserir(lista):

    valor = input("Digite um valor:")

    lista.append(valor)

    print("Valor inserido com sucesso!!")

    input("Aperte qualquer tecla para continuar....")

def Listar (lista, flag):
    
    if not lista:

        print("A lista está vazia!!")
     
    for i, item in enumerate(lista):

        print(f'{i}: {item}')

    if flag == 0:

        input("Aperte qualquer tecla para continuar....")



lista = []


while True:

    os.system('cls')

    entry = input('Selecione uma opção (Se desejar sair digite [s]) \n\n[i]nserir [a]pagar [l]istar:')

    os.system('cls')
    
    if entry == 'i':

        Inserir(lista)

    elif entry == 'a':

        Apagar(lista)

    elif entry == 'l':

        Listar(lista, 0)

    elif entry == 's':
        break

    else:

        print('Tente novamente')




