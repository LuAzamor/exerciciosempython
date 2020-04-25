consumo= int (input ("Consumo em kWh:  "))
instalacao= (input ("Tipo de instalação: R, C ou I? "))

if instalacao == "R" and consumo <= 500:
    preco_kWa = 0.40

elif instalacao == "R" and consumo > 500:
    preco_kWa = 0.65

elif instalacao == "C" and consumo <= 1000:
    preco_kWa = 0.55

elif instalacao == "C" and consumo > 1000:
    preco_kWa = 0.60

elif instalacao == "I" and consumo <= 5000:
    preco_kWa = 0.55

elif instalacao == "I" and consumo > 5000:
    preco_kWa = 0.60
    
else:
    print ("categoria invalida")
    
a_pagar = preco_kWa * consumo

print ("sua conta será de: R$ %0.2F" %a_pagar)   