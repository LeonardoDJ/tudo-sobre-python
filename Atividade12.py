lista1 = []
lista2 = []
lista3 = []

for numero1 in range(1,7):
    numeros = int(input("Digite os numeros da primeira lista: "))
    lista1.append(numeros)

print("\nSegunda Lista")

for numero2 in range(1,7):
    numeros = int(input("Digite os numeros da segunda lista: "))
    lista2.append(numeros)
    
for i in range(6):
    lista3.append(lista1[i] + lista2[i])
    
print(f"lista 1: {lista1}")
print(f"lista 2: {lista2}")
print(f"Lista resultante: {lista3}")