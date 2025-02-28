

def mult (*args):

    total = 1

    for num in args:
        total *= num

    return total

x = []


while True:

    value = input("Digite os números para serem multiplicados:")
    
    if value == 's':
        break

    x.append(int(value))

# print(x)
# print(*x)

mul = mult(*x)
print(f"O valor obtido da multiplicação foi {mul}")


def is_pair (num):

    return (num % 2 == 0)

x1 = int(input("Digite um número para verificar se é par ou ímpar:"))

x1 = is_pair(x1)

if x1:
    print("O valor é par!!")
else:
    print("O valor é ímpar")
