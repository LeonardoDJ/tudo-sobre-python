soma = 0

numero = int(input("Digite o numero da tabuada q vc quer: "))

for i in range(1,11):
    valor = i * numero
    soma += 1
    print(f"{soma} x {numero} = {valor}")