nome = input("Informe seu nome: ")
nota = float(input('Digite sua nota (0 a 10): '))

if (nota == 10):
  print('Parabéns {}! Você é 10!'.format(nome))
elif (8<=nota<10):
  print('Parabéns {}! Você brilhou!'.format(nome))
elif (6<=nota<8):
  print('Bom trabalho, {}! Você está na média'.format(nome))
elif (4<=nota<6):
  print('{}... Você precisa melhorar'.format(nome))
elif (2<=nota<4):
  print('Vamos lá, {}! Você é melhor que isso'.format(nome))
elif (nota<0 or nota>10):
  print('Quê isso cara... Essa nota não existe...')
else: 
  print('Burro...')
  