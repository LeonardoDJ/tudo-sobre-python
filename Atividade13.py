produto = {}

for i in range(3):
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    preco = float(input("Preço do produto: R$"))
    produto[nome] = [descricao, preco]
    
nome_caro = ""
maior_preco = 0

for nome, dados in produto.items():
    if dados[1] > maior_preco:
        maior_preco = dados[1]
        nome_caro = nome

print("O produto mais caro é:", nome_caro)
print("Preço: R$", maior_preco)