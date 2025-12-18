import json

# pessoa = {
#     'nome': 'Samuel',
#     'sobrenome': 'Vasdcasd',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 22},
#         {'rua': 'R2', 'numero': 77},
#     ],
#     'altura': 1.78,
#     'numeros_preferidos': (7, 17, 10 , 8, 26),
#     'dev': True,
#     'nada': None,
# }

# with open('aula120.json', 'w', encoding='utf8') as arquive:
#     json.dump(pessoa, arquive, indent=2)
    

with open('aula120.json', 'r', encoding='utf8') as arquive:
    pessoa = json.load(arquive)
    print(pessoa['nome'])
    print(pessoa)