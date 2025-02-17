""" Calculadora """
import os

def get_number ():

    while True:

        try:

            n = (float(input('Digite um número:')))

            return n
        
        except:

            print("Você não digitou um número, por favor tente novamente!")

def get_operator ():

    operators = ['+','-','*','/','**']
    
    while True:
        
        op = (input('Digite um operador matemático:'))

        if(op in operators):

            return op
        
        else:

            print('Você não digitou um operador válido, por favor tente novamente!!!')

def calculate_operation(n1, n2, op):

    if op == '+':

        return n1 + n2
    
    elif op == '-':

        return n1 - n2
    
    elif op == '*':

        return n1 * n2
    
    elif op == '/':

        return n1 / n2
    
    else:

        return n1 ** n2


while True:

    
    n1 = get_number()
    n2 = get_number()
    op = get_operator()


    result = calculate_operation(n1, n2, op)

    print (f"O resultado da operação é {result:,.2f}")



    exit = input('Deseja sair? [s]im: ').lower().startswith('s')

    os.system('cls')

    
    if exit:

        break
    
    


        

