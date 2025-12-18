# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


def list_all():
    if not todo_list:
        print('Empty list!')
        return
    print('Task list:\n')
    for task in todo_list:
        print(f'{task}')
    print('\n')

def redo_one():
    if not redo_list:
        print('Empty list!')
        return
    todo_list.append(redo_list.pop())

def undo_one():
    if not todo_list:
        print('Empty list!')
        return
    redo_list.append(todo_list.pop())

def add_list(content):
    todo_list.append(content)


todo_list = list()
redo_list = list()

print("Comands: list, redo, undo, clear, exit\n")

while True:

    command = input ("Put any task or command:").lower()


    match command:

        case 'list':
            list_all()

        case 'redo':
            redo_one()

        case 'undo':
            undo_one()

        case 'clear':
            os.system('cls')

        case 'exit':
            exit(0)

        case _: add_list(command)