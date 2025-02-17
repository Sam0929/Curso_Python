name = input ("Digite seu nome:")
age = input("Digite sua idade:")

if (name and age):

    print(f"Seu nome é {name}")
    print(f"Seu nome invertido é {name[::-1]}")

    if (" " in name): 
        print(f"Seu nome contém espaços")
    else:
        print(f"Seu nome NÃO contém espaços")

    print(f"Seu nome tem {len(name)} caracteres")
    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A última letra do seu nome é {name[-1]}")

else:

    print("Desculpe, seu nome ou sua idade não foi preenchida corretamente")


