letras = {}

frase = input("Digite uma frase para contar as letras: ")

for caractere in frase:
    if caractere in letras:
        letras[caractere] += 1
    else:
        letras[caractere] = 1
        
print(letras)