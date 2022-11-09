'''

count = 1 
print(count)
count = count+1
print(count)
count +=1
print(count)

'''

count = 1

while(count<=10):
  print(count)
  count +=1


#foreach
#lista -> vetor
frutas = ['maçã', 'banana', 'laranja']

#incluir no final da lista
frutas.append('maracujá')

for x in frutas:
  print(x)


#exibir apenas uma fruta em um índice específico
print(frutas[2])

#Quantidade de frutas na lista
y = len(frutas)
print('A quantidade de frutas é: ',y)

#usando while
i=0
while(i<len(frutas)):
  print(frutas[i])
  i+=1

