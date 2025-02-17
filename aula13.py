# Introdução à f-strings


nome = "Samuel Vanini"
altura = 1.78
peso = 70
imc = (peso / altura ** 2)
dinheiro = 1000323.28


linha1 = f"{nome} tem {altura} de altura\npesa {peso} quilos, seu IMC é: {imc:.2f} e tem R$: {dinheiro:,} de reais"  #colocar f antes de uma string permite usar {} para ser interpretado como variáveis
# é possível fazer {dinheiro:,.2f}



print (nome, "tem", altura, "de altura,\npesa", peso, "quilos e seu IMC é:", round(imc, 2), "aproximadamente.")



print(linha1)

# ... é Ellipsis, usado para deixar "reservado" um espaço que posteriormente terá um código

imc = ...   #exemplo
