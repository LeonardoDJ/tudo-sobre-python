prec_original = float(input("O preço original do produto: "))
desconto_concedido = float(input("Desconto que irá receber o produto: "))

if prec_original <= 0:
    print("O preço está errado!")
else:

    prec_desconto = (prec_original * desconto_concedido) / 100
    total_produto =  prec_original - prec_desconto

    print(f"O valor original do produto é: R$ {prec_original:.2f}")
    print(f"Você deu um desconto de R${desconto_concedido}")
    print(f"O valor do produto com o desconto é: R$ {total_produto:.2f} ")