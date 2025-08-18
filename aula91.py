#introducao as generator function em Python
#generator = (n for n in range(1000))

def generator(n=0): #se fosse fazer dessa forma seria muito complexo
    return 1
gen = generator()  

#a forma simples de fazer e com yield

def generator (n=0):
    yield 1 # pausar
    return 'Acabou'

gen = generator (n=0)
print(gen)
print(next(gen))
# print(next(gen)) #retorna e stop iteration

def generator2 (n=0):
    yield 1 # pausar
    print('Continuando')
    print('aaaaa')
    yield 2 # pausar
    print('231312321')

gen2 = generator2 (n=0)
print(gen2)
print(next(gen2))
print(next(gen2)) #retorna e stop iteration

for n in gen2:
    print(n)

def generator_th(n, maxi):
    while (n != maxi):
        yield n  #pausa em todos os yield
        n += 1

gen_th = generator_th(0, 100)


for n in gen_th:
    print(n)


