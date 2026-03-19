desconto = 20

prec_original = float(input("O preço original do produto: "))

if prec_original <= 0:
    print("O preço está errado!")
else:
    prec_desconto = (prec_original * desconto) / 100
    total_produto =  prec_original - prec_desconto

    print(f"O valor original do produto é: R$ {prec_original:.2f}")
    print("Você ganhou um desconto de 20%")
    print(f"O valor do produto com o desconto é: R$ {total_produto:.2f} ")