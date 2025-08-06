lista = []
while len (lista) <10:
    num = int(input("Digite um número: "))
    if num in lista:
        print("Números repetidos")
    else:
        lista.append(num)

lista.sort()
print(lista)