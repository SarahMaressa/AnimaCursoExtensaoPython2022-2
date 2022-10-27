# Comando input(): permitir que o usuário digite algo
#Comando de entrada
nome = input("Digite seu nome: ")

#idade = int(input("...")) <- declarar variável como inteira
idade = int(input('Digite sua idade: '))

sexo = input('Informe o seu gênero(M ou F): ')

#Comando de saída
print('Boa noite {}. Sua idade é {}'.format(nome,idade))

# Mostrar o dobro da idade informada
# Guardar variável em um tipo inteiro = int()
dobro = idade * 2

print('O dobro da sua idade é {}'.format(dobro))

# Estrutura condicional - if
# if (idade >= 18):
#  print(...)
if idade >= 18:
  print('Você é maior de idade!')
else:
  print('Você ainda não atingiu a maior idade')

if (idade >=18 and sexo == 'M'):
  print('Você é maior de idade e precisa/precisou servir o exército')
elif idade <18 and sexo == 'M':
  print('Você é menor de idade e deve servir o exército quando atingir 18 anos')
elif idade >=18 and sexo == 'F':
  print('Você é maior de idade e não precisa servir o exército')
else:
  print('Você é menor de idade')
