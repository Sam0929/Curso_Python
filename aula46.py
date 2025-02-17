for i in range(10):

    if i == 2:
        print('i é 2, pulando ...')
        continue      #volta no for

    if i == 8:
        print('i é 8, seu else não executará')
        break         #pula fora


    for j in range(1,3):
        print(i, j)
else:
    print('For completo com sucesso!!')  #só executa se o for completar inteiramente