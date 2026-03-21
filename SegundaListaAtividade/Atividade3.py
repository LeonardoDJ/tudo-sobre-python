frase = input("Escreva uma frase: ")

frase_maiuscula = frase.upper()
frase_sem_espaco = frase.replace(" ", "&")

print(f"A frase que você escrever em maiusculo: {frase_maiuscula}")
print(f"A frase que voce escreveu sem espaco: {frase_sem_espaco}")