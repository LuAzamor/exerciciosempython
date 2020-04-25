valor_casa = float (input ("Valor da casa:  "))
salario= float (input ("Seu salário:  "))
anos= int (input ("Anos a pagar:  "))

prestacao = valor_casa / (anos *12)

if prestacao <= salario * 0.3:
    print ("Emprestimo aprovado! Sua parcela é de R$ %0.2f" %prestacao)

else:
    print("Empréstimo nao aprovado!")
