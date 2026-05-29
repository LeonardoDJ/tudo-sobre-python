numeros = ()

while True:
    numero = int(input("Digite um numero: (lembrando que para sair é '0')"))
    if numero == 0:
        break
    numeros = numeros + (numero,)
    
print("Na tupla tem tantos caracteres, possui: ",len(numeros))
print("Na tupla tem maior possui: ",max(numeros))
print("Na tupla tem menor caracteres, possui: ",min(numeros))