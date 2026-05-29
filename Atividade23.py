numeros = []

for i in range(5):
    numero = int(input("Digite um numero: "))
    if numero > 10:
        numeros.append(numero)
    
print(f"Numeros maiores que 10: {numeros}")