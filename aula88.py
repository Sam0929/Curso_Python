#dir, hasattr e getattr em python
#dir, todos os atributos que estão definidos no objeto
string = "Samuel"
metodo = 'upper1'

if hasattr(string, metodo):
    
    print("Tem o método")
    # print(string.metodo()) não funciona
    print(getattr(string, metodo)()) # busca o método e executa
    #pode ser assim também
    aux = getattr(string, metodo)
    print(aux())
    print(string)

else:

    print(f'Não existe o metodo: {metodo}')