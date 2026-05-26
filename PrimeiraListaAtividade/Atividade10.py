import math

vel_fluido = float(input("Qual a velocidade do fluido no tubo? (m/s): "))
diametro_interno_cm = float(input("Qual o diametro interno do tubo?(cm): "))

# Mudando os valores de cm para metros
diametro_interno_m = diametro_interno_cm / 100

vazao = math.pi * (diametro_interno_m**2 / 4) * vel_fluido

vazao_Ls = vazao * 1000

print(f"A vazão do tubo, é de: {vazao:.2f}, que equivale a: {vazao_Ls:.2f}")