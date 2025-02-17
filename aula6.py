#Conversão de tipos, type convertion, typecasting, coercion
print (1 + 1)

print ('a' + 'b')

#print ('1' + 1) ERRO!!! tipagem forte
#str, int, float e bool são imutaveis

print (int('1') + 1)

#faz mais sentido se

valor = '12'

#print (valor + 2) ERRO!!!!
print (int(valor) + 2) # Agora funciona 

#posso fazer float + int

print (float('1.1') + 2)

#concatenar

print(str(12) + "b")
 
