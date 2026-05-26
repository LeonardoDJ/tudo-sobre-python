import math

raio_maior = float(input("Me fale a medida do circulo maior: "))
raio_menor = float(input("Me fale a medida do circulo menor: "))

area = math.pi * (raio_maior**2 - raio_menor**2)

print(f"A área do circulo é: {area:.2f}cm²")