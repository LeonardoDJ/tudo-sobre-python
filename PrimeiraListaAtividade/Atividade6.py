litro_combustivel = 4.95 
preco_medio_km = 20

gasto_gasolina = float(input("Qual a quantidade que você pretende gastar com o combustivel?: ")) 

total_gasolina = gasto_gasolina / litro_combustivel 
total_quilometros = preco_medio_km * total_gasolina

print(f"A quantidade que voce pode comprar em combustivel R$: {gasto_gasolina}, você pode essa quantidade de litros: {total_gasolina:.2f}L e a quantidade de quilometros que irá percorrer é: {total_quilometros:.2f} km")