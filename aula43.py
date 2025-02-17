# text = 'Python'

# for char in text: # Char = variável criada para guardar os caracteres a cada rep
#     print(char)

text = 'Python'

new_text = ''

for char in text:
    new_text += f'*{char}'

new_text += '*'

print(new_text)