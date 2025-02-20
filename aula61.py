import re
import random


# cpf = '746.824.890-70'

# cpf = re.sub(r'[^0-9]', '','746.824.890-70' )

cpf = ''

for i in range (9):

    cpf += str(random.randint(0,9))


def algoritmo_cpf(digito, cpf):

    i = digito

    valor = 0
    contador = 0

    while contador < (digito - 1):  # Garante que o loop rode exatamente (digito - 1) vezes
        valor += (int(cpf[digito - i]) * i)  # Ajuste no índice do CPF
        i -= 1
        contador += 1  
  
    valor = (valor * 10) % 11
    
    if valor > 9:
        valor = 0
  
    return (cpf + (str(valor)))

 
    
cpf = algoritmo_cpf(10, cpf)

         
cpf = algoritmo_cpf(11, cpf)
print(cpf)
         
