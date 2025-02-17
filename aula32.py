"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

n = None
verified_number = None

# while True:

#     try:
        
#         n = (int(input('Digite um número inteiro:')))
#         verified_number = n % 2

#         break
#     except:
#         print("Você não digitou um número inteiro, por favor tente novamente!")

# if (not verified_number):
#     print (f'Seu número "{(n)}" é par')
# else:
#     print (f'Seu número "{(n)}" NÃO é par')



# while True:

#     try:
#         n = (int(input('Digite que horas são por favor, somente os primeiros digitos(exemplo: São 18:34, digite: 18):')))
#         break
#     except:
#         print("Você não digitou um horário válido, tente novamente!")

# if (n <= 24 and n >= 18):
    
#     print("Boa noite!")
    
# elif (n < 18 and n >= 12):
#     print("Boa tarde!")

# elif(n < 12 and n > 0):
#     print("Bom dia!")
# else:
#     print("Você não digitou um horário válido!!")


name = input("Digite seu nome:")

tam = len(name)

if(tam <= 4):
    print("Seu nome é curto")
elif(tam <=6):
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande!")



