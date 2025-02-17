#Usando inputs

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}') #Usar {nome=} para imprimir o nome da variável e a variável em seguida
print(f'{nome=}') 



while True:
    numero_1 = input('Digite um número: ')
    try:

        numero_valido = float(numero_1)
        break
    except:
        
        print('Isso não é um valor válido, tente novamente!')

print(numero_valido)
