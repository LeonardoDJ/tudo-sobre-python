comeco = 1

n = int(input("Digite um numero para eu fazer o Tringulo de Floyd: "))

for i in range(1, n +1):
    for j in range(i):
        print(comeco, end=" ")
        comeco += 1
    print()
    