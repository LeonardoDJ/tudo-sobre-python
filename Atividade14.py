pessoas = {}
nomes = []

for i in range(15):
    nome = input("Seu nome: ")
    altura = float(input("Sua altura: "))
    peso = float(input("Seu peso: "))
    pessoas[nome] = [altura, peso]

menor_altura = 999
nome_baixo = ""
peso_medio = 0

for nome, dados in pessoas.items():
    if dados[0] < menor_altura:
        menor_altura = dados[0]
        nome_baixo = nome

for nome, dados in pessoas.items():
    peso_medio += dados[1]
    
media = peso_medio/len(pessoas)

for nome in pessoas:
    nomes.append(nome)
nomes.sort()

print("Menor altura é:", menor_altura)
print("Peso médio das pessoas é:", media)
print("Ordem alfabetica: ", nomes)