"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

secret_word = 'secret'
count = 0
correct_chars = ''

while True:

    letter = input (f"Digite uma letra [{count:01x}]:")

    if(len(letter) == 1 and letter.isalpha()):

        count += 1

        if letter in secret_word:
            correct_chars += letter

    else:

        print("Por favor, digite apenas uma letra!!")
        continue
    
    writed_word = ''

    for char in secret_word:

        if char in correct_chars:
            writed_word += char
            
        else:

            writed_word += "*"

    print(writed_word)

    if (writed_word == secret_word):

        print('Parabéns, você acertou a palavra!!!')

        break
           



