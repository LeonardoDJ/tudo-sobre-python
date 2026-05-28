temperatura_media_mes = []

for media in range(12):
    temp = float(input(f"Temperatura media do mês {media + 1}: "))
    temperatura_media_mes.append(temp)
    
soma = 0
    
for medias in temperatura_media_mes:
    soma += medias
    
media_anual = soma/12

for i, tem_media in enumerate(temperatura_media_mes):
    if tem_media > media_anual:
        print(f"Mês {i + 1} está acima da média: {tem_media}°C")