"""
Introdução ao try/except

"""

while True:

    try:
        n = (float(input('Digite um número:')))
        break
    except:
        print("Você não digitou um número, por favor tente novamente!")

print (f'O dobro do seu número é: {(n*2):.2f}')