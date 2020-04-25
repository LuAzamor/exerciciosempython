quantidade_impares= int (input("Digite o n: "))
quantidade_impresso = 0
numero = 0

while quantidade_impresso < quantidade_impares:
    if numero % 2 != 0:
        print (numero)
        quantidade_impresso = quantidade_impresso + 1
    numero = numero + 1