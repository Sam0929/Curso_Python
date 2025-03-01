# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

#sets parecem um dicionario, porem so possuem valor


s1 = set('Luiz')
s1 = {'Luiz', 1, 2, 3}
print(s1, type(s1))


# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s1 = {1, 2, 3, 4, 5, 3, 3, 3, 3, 2, 2, (1, 2, 3)} #sets eliminam valores duplicados automaticamente
print(s1)                              #sets não aceitam valores mutáveis, somente imutáveis

# Métodos úteis:
# add, update, clear, discard