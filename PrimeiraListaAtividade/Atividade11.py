peso = float(input("Qual seu peso: "))
altura = float(input("Qual sua altura: "))

IMC = peso / ((altura/100) ** 2)

if IMC <= 18.5:
    print(f"Você está a baixo do peso normal: {IMC:.1f}")
elif IMC >= 18.5 and IMC <=24.9:
    print(f"Você está no peso normal: {IMC:.1f}")
elif IMC >= 25.0 and IMC <=29.9:
    print(f"Você está em excesso de peso: {IMC:.1f}")
elif IMC >= 30.0 and IMC <= 34.9:
    print(f"Você está em obesidade classe 1: {IMC:.1f}")
elif IMC >= 35.0 and IMC <=39.9:
    print(f"Você está em obesidade classe 2: {IMC:.1f}")
else:
    print("Você está na obesidade classe 3!")