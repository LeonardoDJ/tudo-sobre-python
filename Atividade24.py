alunos = {}

for i in range(3):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))
    
    alunos[nome] = nota

for nome,nota in alunos.items():
    if nota >= 7:
        print(f"As notas dos alunos foram: {nome}: {nota}")
    