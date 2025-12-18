# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

path = 'C:\\Users\\Samuel\\WorkSpace\\Curso_Python_3\\folder_test\\test.txt'

# arquive = open(path, 'w')

# arquive.close()

with open(path, 'w+') as arquive:
    arquive.write('Hello\n')
    arquive.write('Hello again\n')
    arquive.writelines(('ONE\n', 'TWO\n', 'THREE\n'))

    arquive.seek(0,0)
    print(arquive.read())

    arquive.seek(0,0)
    print(arquive.readline())

    arquive.seek(0,0)
    for line in arquive.readlines():
        print(line.strip())
    

# with open(path, 'r') as arquive:
#     print(arquive.read())

with open(path, 'a+') as arquive: #append mode, escreve ao final
    arquive.write('Hello\n')
    arquive.write('Hello again\n')
    arquive.writelines(('ONE\n', 'TWO\n', 'THREE\n'))