produtos = {}

for i in range(5):
    produto = input("Qual o produto vai adicionar? ")
    preco = float(input("Qual o preco do produto? "))
    
    produtos[produto] = preco
    
for produto,preco in produtos.items():
    if preco <= 50:
        print(f" O produto:{produto} tem o preco de: R${preco}")