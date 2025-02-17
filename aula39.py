
while True:

    name = input('Digite seu nome:')


    if name.isalpha():

        break

    else:
    
        print("Você não digitou um nome, por favor tente novamente!")

name_wid = len(name)
new_name = ""
i = 0

while (i < name_wid):

    new_name += f'*{name[i]}'
    i += 1

new_name += '*'     

print(new_name)


