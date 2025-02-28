# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

number = 0

number = int(input("Enter a number:"))

def mult_create(times):
    def mult(num):
        return num * times
    return mult

mult_2 = mult_create(2)                                      #Vantages de utilizar closure, reduzir a criacao de funcoes em uma linha
mult_3 = mult_create(3)        
mult_4 = mult_create(4)

print(f'Number multiplied by 2: {mult_2(number)}')
print(f'Number multiplied by 3: {mult_3(number)}')
print(f'Number multiplied by 4: {mult_4(number)}')
