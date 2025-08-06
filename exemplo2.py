import random
from collections import Counter
print("--------------Loto Fácil-------------------- ")
lista =[]
# 1 a 25 --> 15 números simule 100.000 jogos e indique os 15 números que mais apareceram
for i in range (100000):
  jogo = random.sample (range(1,26),15)
  lista.append(jogo)

todos_numeros = [num for jogo in lista for num in jogo]
contagem = Counter(todos_numeros)
mais_comuns = contagem.most_common(15)

print("Os 15 números que mais apareceram são:")
for numero, frequencia in mais_comuns:
    print(f"Número {numero}: apareceu {frequencia} vezes")




#jogo = random.sample (range(1,25),15)
#print(jogo)



