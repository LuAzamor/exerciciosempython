## Criação de uma lista com o quadrado de todos os números inteiros de 1 a 10.

quadrados = []  # cria uma lista vazia.
for valor in range(1,11):
    quadrado = valor ** 2
    quadrados.append(quadrado) # a lista recebe o quadrado de cada elemento do intervalo.
    print (quadrados) # Saída: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


## exemplo de for dentro de for. Tabuada de 2 e 3!0

for i in range(2,4):              # abaixo o bloco de execucao do for externo
    print("Tabuada do " + str(i))
    for j in range(0,11):
        print(str(j) + " " + str(j * i))