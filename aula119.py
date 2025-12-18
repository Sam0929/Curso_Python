## ENCODING and OS REMOVE/UNLINK

import os

path = 'C:\\Users\\Samuel\\WorkSpace\\Curso_Python_3\\folder_test\\test.txt'

with open(path, 'w', encoding='utf8') as arquive: #append mode, escreve ao final
    arquive.write('Atenção\n')
    arquive.write('Hello\n')
    arquive.write('Hello again\n')
    arquive.writelines(('ONE\n', 'TWO\n', 'THREE\n'))


# os.remove(path)