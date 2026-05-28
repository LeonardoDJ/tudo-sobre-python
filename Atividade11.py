x = int(input("Digite algum valor de x: "))
y = int(input("Digite algum valor de y: (lembrando que esse valor tem q ser um numero maior q o x)"))
if x < y:
    resultado = list(range(x,y + 1))
    print(f"A lista dos numeros de {x} e {y} é: {resultado} ")
else:
    print(f"O valor de y: {y} é menor que do x: {x}!")