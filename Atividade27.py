aluno = {}

while True:
    nome = input("Qual seu nome? (caso queira sair, digite'sair')")
    if nome == "sair" or nome == "Sair":
        break
    idade = int(input("Qual sua idade? "))
    aluno[nome] = idade
    
print(f"Todos os alunos cadastrados: ",(aluno))