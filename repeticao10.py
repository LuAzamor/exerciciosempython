# pergunta depósito inicial e a taxa de juros de uma poupança, exibe os valores mês a mês para 24 meses, e o total de ganho com jurus

deposito = float (input ("Valor do depósito: "))
taxajuros = float (input ("Taxa de juros: "))

x = 1

while True:
    x = x + 1
    n = deposito / taxajuros    # taxa de juros mensal
    n = n + n

print (deposito + n)
