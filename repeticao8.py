#soma de 10 números digitados pelo usuário


n = 1
soma = 0

while n <= 10:
    x = int (input ("Digite o %d número: " %n))
    soma = soma + x
    n = n + 1

print ("Soma: %d" %soma)