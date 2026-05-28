lista_numeros = []

for i in range(5):
    numeros = int(input("Digite um numero: "))
    if numeros not in lista_numeros:
        lista_numeros.append(numeros)

print(lista_numeros)
  
