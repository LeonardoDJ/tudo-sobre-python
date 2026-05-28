numero = int(input("Digite um numero de 100 a 999: "))
if numero >= 100 and numero <= 999:
    inteiro = numero//100
    resto = numero % 100
    dezena = resto // 10
    unidade = resto % 10
    print(inteiro)
    print(dezena)
    print(unidade)
else:
    print("NUMEROS ENTRE 100 À 999!!")