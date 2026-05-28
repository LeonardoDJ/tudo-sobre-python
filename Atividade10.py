funcionario = {}

for i in range(1,3):
    ind_numerico = int(input("Qual o indidice? "))
    nome = input("Qual seu nome? ")
    funcao = input("Qual sua função? ")
    temp_servico = int(input("Quanto tempo de serviço? (Em anos) "))
    func = []
    func.append(nome)
    func.append(funcao)
    func.append(temp_servico)
    funcionario.update({ind_numerico:func})

input(f"Todos os funcionarios cadastrados: {funcionario} (digite 'Enter' para continuar)")

demitir = int(input("Digite o indice do funcionario a demitir: "))
func_escolhido = funcionario[demitir]
if func_escolhido[1] == "Programador" and func_escolhido[2] >= 3:
    print(f"Este funcionario nao pode ser demitido!")
else:
    del funcionario[demitir]
    print(f"Funcionario restante: {nome}, {funcao}")   
    