lista = []
num = int(input("Digite um número inteiro: "))
lista.append(num)

for _ in range (10):
    num = int(input("Digite um número inteiro: "))
    if num in lista:
        print("Número já digitado, interrompendo.")
        num = int(input("Digite um número inteiro: "))
    else:
        lista.append(num)
lista.sort()
print(lista)


