pedido_lapis = int (input ("Digite quantos lapis quer comprar: "))
pedido_caneta = int (input ("Digite quantas canetas quer comprar: "))
pedido_resma = int (input ("Digite quantas resmas quer comprar: "))

unid_lapis = 1.85 
unid_caneta = 4.99
unid_resma = 19.90

total = (pedido_lapis * unid_lapis) + (pedido_caneta * unid_caneta) + (pedido_resma * unid_resma)

print ("O pedido foi de", pedido_lapis, "lápis,", pedido_caneta, "canetas e", pedido_resma, "resmas." )

print ("O total da compra é de R$ %.2f "  %total)