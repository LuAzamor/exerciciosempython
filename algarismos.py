numero = int(input("Numero: "))
soma = 0

while (numero != 0):
    restante = numero % 10
    numero = (numero - restante)//10
    soma = soma + restante
print(soma)