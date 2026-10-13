# input(): Comando de entrada de dados. Lê o que o usuário digita no teclado e guarda como texto na variável 'nome'
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
# print(): Comando de saída de dados. Exibe valores e variáveis na tela (quando separados por vírgula, insere um espaço automaticamente)
print(nome, idade, peso)

#Atividade01
#Crie um script de python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
nome = input("Digite seu nome: ")

# + (Operador de Concatenação): Usado para juntar/colar textos e variáveis dentro do print
print("Bem-vindo(a), " + nome + "! É um prazer ter você aqui.")

#Atividade02
#crie um script em python que leia o dia, mês o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

dia = input ("Digite sua data de nasciment(DD):")
mes = input ("Digite usa data de nascimento(MM):")
ano = input ("Digite sua data de nascimento(AAAA):")
print ("Sua data de nascimento é: " + dia + "/r" + mes + "/" + ano)
