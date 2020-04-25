# calcula a média aritimética de 5 números digitados pelo usuário
#acumula ao invés de criar 5 variáveis diferentes

x = 1
soma = 0

while x <= 5:
    n = int (input ("%d Digite o número: " % x))
    soma = soma + n                                 # soma acumula os valores de n a cada repetiçao
    x = x + 1                                       # recebe 1 a cada passagem

print ("Média: %.2f" % (soma / 5))
