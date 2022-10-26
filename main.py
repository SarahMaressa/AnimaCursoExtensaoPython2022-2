# Comando input(): permitir que o usuário digite algo
#Comando de entrada
nome = input("Digite seu nome: ")

#idade = int(input("...")) <- declarar variável como inteira
idade = input('Digite sua idade: ')

#Comando de saída
print('Boa noite {}. Sua idade é {}'.format(nome,idade))

# Mostrar o dobro da idade informada
# Guardar variável em um tipo inteiro = int()
dobro = int(idade) * 2

print('O dobro da sua idade é {}'.format(dobro))