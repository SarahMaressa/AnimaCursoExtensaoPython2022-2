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
print(preco + calcular_imposto(preco))
#imposto = calcular_imposto(preco)
#total = preco + imposto
#print(total)

valores = [1.99, 24.50, 78.27, 1515.5]

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto(valor)}")

# Declarar uma função calcular_imposto_aliquota que recebe dois parametros
# O preço do produto e a aliquota de imposto a ser aplicada
# Se a aliquota não for informada, utilize 7% como padrão

def calcular_imposto_aliquota(valor, aliquota = 7):
  imposto = valor * aliquota/100
  return imposto

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor)}")

for valor in valores:
  print(f"O imposto de {valor} é {calcular_imposto_aliquota(valor, 5)}")
















  

