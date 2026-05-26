import math

r = float(input("Digite o raio para calcular a área do hexágono: "))

angulo_radianos = math.radians(60)
seno = math.sin(angulo_radianos)

area_triangulo = (r * r * seno) / 2
total_hexagono = area_triangulo * 6

print(f"A área do hexagono a partir do valor do raio: {r:.2f}, é de: {total_hexagono:.2f}")

