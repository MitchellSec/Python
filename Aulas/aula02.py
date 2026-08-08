# --- BLOCO 1: Soma simples com conversão para inteiro ---

# int(): Converte o texto digitado no input() para número inteiro
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('A soma é', n1 + n2)


# --- BLOCO 2: Armazenando a soma e formatando a saída ---

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

s = n1 + n2

# .format(): Substitui o {} dentro da frase pelo valor armazenado na variável
print('A soma é {}'.format(s))


# --- BLOCO 3: Verificação do tipo da variável e formatação avançada ---

n1 = input('Digite um valor: ')

# type(): Exibe o tipo primitivo da variável (ex: <class 'str'> ou <class 'int'>)
print(type(n1))

n2 = int(input('Digite um valor: '))
print(type(n1))

s = n1 + n2
print('A soma entre', n1, 'e', n2, 'é', s)

s = n1 + n2

# O .format() insere os valores sequencialmente em cada um dos marcadores {}
print('A soma entre {} e {} é {}'.format(n1, n2, s))
