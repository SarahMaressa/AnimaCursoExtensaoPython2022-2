# Criação de funções
preco = 1999.90

# Calcular 5% de imposto, guardar na variável de imposto e exibir na tela
imposto = preco * 0.05
print(imposto)

# Criar uma função calcular_imposto() que calcula um imposto de 5% e retorna a quem pediu...
# Declaração da função
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

# Uso da função
preco = 299
imposto = calcular_imposto(preco)
total = preco + imposto
print(total)
