produtos = {}
total_geral = 0

while True: 
    cod = int(input("Codigo do produto: (Caso queira sair, digiti '0')"))
    if cod == 0:
        break
    nome = input("Nome do produto: ")
    prec_unit = float(input("Preço unitario do produto: "))
    qtd = int(input("Quantidade do produto: "))
    produtos[cod] = (nome, prec_unit, qtd)
    
for cod,valores in produtos.items():
    nome = valores[0]
    prec_unit = valores[1]
    qtd = valores[2]
    subtotal = qtd * prec_unit
    total_geral +=subtotal 
    print(f"O valor subtotal da compra de cada item é: {subtotal} do produto {nome}")
    
print(f"Subtotal de {nome}: R$ {subtotal:.2f}")
    

    