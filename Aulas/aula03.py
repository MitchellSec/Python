# LEITURA DE DADOS E VERIFICAÇÃO DE TIPOS
a = input('Digite seu nome: ')

print('Seu nome é: {}'.format(a))
print('O tipo primitivo de a é {}'.format(type(a)))

# .isspace(): Retorna True se a variável contiver apenas espaços em branco
print('Tem espaços?', a.isspace())

# .isnumeric(): Retorna True se a variável contiver apenas números (dígitos)
print('Tem números?', a.isnumeric())

# .isalpha(): Retorna True se a variável contiver apenas letras do alfabeto
print('É alfabético?', a.isalpha())

# .isalnum(): Retorna True se contiver letras e/ou números (alfanumérico)
print('É alfanumérico?', a.isalnum())

# .isupper(): Retorna True se todas as letras estiverem em MAIÚSCULAS
print('É maiúsculo?', a.isupper())

# .islower(): Retorna True se todas as letras estiverem em minúsculas
print('É minúsculo?', a.islower())

# .istitle(): Retorna True se estiver capitalizada (primeira letra de cada palavra maiúscula)
print('Está capitalizada?', a.istitle())
