numeros = []

for i in range(5):
    numero = int(input("Digite algum valor: "))
    numeros.append(numero)
        
maior = max(numeros)
minimo = min(numeros)        

print(f"Maior: {maior}")
print(f"Minimo: {minimo}")