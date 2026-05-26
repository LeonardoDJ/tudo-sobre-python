d = {}

while True:
    nome = input("Qual seu nome? (Caso queira, digite '0'")
    if nome == "0":
        break
    idade = int(input("Qual sua idade? "))
    endereco = input("Qual seu endereço? ")
    telefone = float(input("Qual seu telefone? (9 numeros!)"))
    d[nome] = (nome, idade, endereco, telefone)
    
for chave,valores in d.items():
    nome = valores[0]
    idade = valores[1]
    endereco = valores[2]
    telefone = valores[3]
    print(f"As informacoes da pessoa {nome}, são: {idade}, {endereco}, {telefone}")
