par = []
impar = []

for i in range(6):
    numero = int(input("Digite um numero inteiro: "))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(par)
print("Soma dos numeros pares: ", sum(par))
print("Quantidade de numeros: ",len(par))
print(30*"-")
print(impar)
print("Soma dos numeros impares: ",sum(impar))
print("Quantidade de numeros: ",len(impar))