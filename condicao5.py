distancia_viagem = float (input("qual a distancia, em km, do trecho de sua viagem?"))

base = distancia_viagem
valor_a_pagar = 0


if base <= 200:
    valor_a_pagar = valor_a_pagar + (base * 0.50)

else:
    valor_a_pagar = valor_a_pagar + (base * 0.45)

print ("o custo da sua viagem será de %.2f " %valor_a_pagar)