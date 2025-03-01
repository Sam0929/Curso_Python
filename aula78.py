# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

# for dic in perguntas:

#     respostas += (dic.popitem())

# for string in respostas:
#     respostas.remove("Resposta")

for pergunta in perguntas:
    
    os.system('cls')

    opcoes = pergunta.get('Opções')

    

    while True:

        print(f'Pergunta: {pergunta.get('Pergunta')}\n')

        print('Opcoes:\n')

        for i, opcao in enumerate(opcoes):
        
                print(f'{i}) {opcao}\n')
        try:

            resposta = int(input("Escolha uma opcao:"))

            if resposta < len(opcoes) and resposta >= 0:
                break
            else:
                print("Opção fora do intervalo. Tente novamente!!")
                
        except ValueError:

            print('Digite uma opcao válida!')
            

    if opcoes[resposta] == pergunta.get('Resposta'):
        print('\nParabéns, você acertou!!!👍👍')
        input("Digite qualquer coisa para próxima pergunta")
    else:
        print('\nSinto muito, você errou!❌')
        input("Digite qualquer coisa para próxima pergunta")