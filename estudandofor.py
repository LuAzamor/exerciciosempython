# o comando for deve para listas! De números ou textos. Trabalha com uma variável temporária. No caso abaixo, é a "material"

####################   P/ LISTAS DE NOMES   ######################
materiais = ['caneta', 'caderno', 'livro', 'e-book'] 
for material in materiais:   # material é uma variável temporária.
    print(material)    # imprime caneta, caderno, livro, ebook. Um embaixo do outro.


for material in materiais: 
    print(material.title())    # imprime Caneta, Caderno, Livro, Ebook. Um embaixo do outro.
print(len(materiais))          # imprime - fora do for - o tamanho da lista


####################   P/ LISTAS DE NÚMEROS   ######################

for valor in range(1,5):  # especificamos um intervalo no comando range(), em que o primeiro número indica o primeiro número do intervalo e o Python irá parar no segundo valor especificado (quando ele for atingido). Portanto, o mesmo não será exibido pelo comando print().
    print(valor)          # imprime a lista [1, 2, 3, 4]. O comando range gerou a lista numérica.



# Abaixo a criação de uma lista com o quadrado de todos os números inteiros de 1 a 10.

quadrados = []  # cria uma lista vazia.
for valor in range(1,11):
    quadrado = valor ** 2
    quadrados.append(quadrado) # a lista recebe o quadrado de cada elemento do intervalo.
    print (quadrados) #Saída: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


## Número mínimo da lista 
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
print(min(digitos)) # Saída: 0

## Número máximo da lista 
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
print(max(digitos)) # Saída: 9


## Número máximo da lista 
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] 
print(sum(digitos)) # Saída: 45

#para cada item da lista, faça....
#for item in nome da lista:
#   comando vai usar variavel item

frutas_exoticas = ["jabuticaba", "cupuaçu", "graviola"]

for fruta in frutas_exoticas:
    print("Eu adoro " + fruta)

#funcao range (siginifica um intervalo)
#sintaxe1:
for i in range(fim):
    comando

#sintaxe2:
for i in range(ini, fim):
    comando

#sintaxe3:
for i in range(ini, fim, passo):
    comando


#exemplo:
pares = range (0, 40, 2) #aqui 2 siginifica um passo, de 2 em 2, imprimindo os numeros pares até 40

for i in pares:
    print(i)

#sintaxe4:
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

for x in range(len(pares)):
    print(x)   #atencao!!!! imprime o 14 primeiros numeros, de zero até 14, pois a lista tem 14 elemntos. Esse comando nao é usual, apenas para eviar erros!!

#Sintaxe5:
pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]
for x in range(len(pares)):
    print(pares[x]) # atencao!!! imprime todos os valores da lista pares

#sintaxe5:
for i in range(16,4,-3):
	print(i)  # imprime os numeros entre 16 e 4, diminuindo 3....(16,13,10,7)~

#sintaxe6:
valores = []  #cria uma lista com numeros pares de 1 a 10. Para ver, dei um print da lista.
for i in range(1, 10):
    if i % 2 == 0:
        valores.append(i)

print(valores)

#sintaxe7:
valores = []  #cria uma lista os numeros de 1 a 9, com intervalos de 2. [1, 3, 5, 7, 9]
for i in range(1, 10, 2):
    valores.append(i)

print(valores)

#sintaxe8:
valores = []  #cria uma lista dos numeros de 1 a 10.
for i in range(0, 10):
    valores.append(i+1)

print(valores)