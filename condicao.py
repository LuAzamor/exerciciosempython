consumo= int (input ("Consumo em kWh:  "))
instalacao= (input ("Tipo de instalação: R, C ou I? "))
    
if instalacao == "R":
    if consumo > 500:
        preco_kWa = 0.65
    else:
        preco_kWa = 0.40
elif instalacao == "C":
    if consumo > 1000:
        preco_kWa = 0.60
    else:
        preco_kWa = 0.55
elif instalacao == "I":
    if consumo > 5000:
        preco_kWa = 0.60
    else:
        preco_kWa = 0.55
else:
    consumo = 0
    preco_kWa = 0
    print("burro do kct")
    
a_pagar = preco_kWa * consumo

print ("sua conta será de: R$ %0.2F" %a_pagar)    