dezena1 = int(input("Digite um número inteiro terminado por zero: "))
dezena2 = int(input("Digite um número inteiro terminado por zero: "))
dezena3 = int(input("Digite um número inteiro terminado por zero: "))
dezena4 = int(input("Digite um número inteiro terminado por zero: "))

dezenas = [dezena1, dezena2, dezena3, dezena4]

dezenas.sort()  
print(dezenas)  # imprime a lista materiais já em ordem ascendente

dezenas.sort(reverse= True)  # ordena os elementos em ordem inversa
print(dezenas)
