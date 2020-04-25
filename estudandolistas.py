materiais = ['caneta', 'caderno', 'livro', 'e-book']

print (materiais [0]) # imprime o elemento correspondente à posição zero

print (materiais [-1]) # imprime o último elemento da lista

print(len(materiais)) # imprime a quantidade de elemnentos da lista

#################################   FATIAMENTO DE LISTA ##############################

print(materiais[0:3]) # saída: ['caneta', 'caderno', 'livro']. Imprime até a posição 2. 3 é o corte!

print(materiais[2:]) # saída: ['livro', 'e-book']. Imprime da posição 2 até o final da lista.

print(materiais[:3]) # saída: ['caneta', 'caderno', 'livro']. Imprime do início da lista até a posição 2.


############################ ALTERAÇÃO ###########################

materiais [2] = 'papel' # modifica o conteúdo da posição 2. Neste caso de 'caderno' para 'papel'


############################ ADIÇÃO ##############################

materiais.append ('borracha') #pode fazer por partes tb. Primeiro adiciona novo elemennto ao final da lista. Append adiciona sempre no final da lista.
print (materiais)   #depois imprime 

materiais.insert (0, 'borracha') # diferente do append, o insert permite especificar a posição do elemento a ser inserido
print (materiais) # 

print (materiais.index ('borracha')) # imprime a posição do elemento na lista. 


############################ ORDENAÇÃO ##########################

materiais.sort ()  
print (materiais)  # imprime a lista materiais já em ordem ascendente

materiais.sort (reverse= True)  # ordena os elementos em ordem inversa

materiais.reverse() 
# não ordena os elementos, ele simplesmente inverte a ordem


############################ DELEÇÁO ############################

del materiais[0]   
print (materiais) # imprime a lista sem o elemento da posição zero removido

del materiais[1:3]  # dá pra remover uma fatia tb


materiais.pop () # remove o último elemento da lista
elemento_removido = materiais.pop () # Pode-se tb armazenar o elemento removido numa variável
print (materiais)
print (elemento_removido)  # mostra o elemento que foi removido

materiais.remove ('caneta') # remove o elemento com o valor especificado

###########################  CLONE DE LISTA ######################

lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1
lista[0] = "rosa"  #vai alterar lista2 e lista1!!!!

#para alterar só uma, terá que fazer um clone:
lista2 = lista1[:]

#EXEMPLO:
materiais = [1, 2, 3, 4]
objetos = materiais[:]    # copia a lista inteira sem especificar os elementos
objetos.append(5)
print(materiais)          # saída: [1, 2, 3, 4]
print(objetos)            # saída: [1, 2, 3, 4, 5]

###################### PERTINÊNCIA A UMA LISTA .... SE X ESTÁ NA LISTA

lista1 = ["vermelho", "verde", "azul"]
"rosa" in lista1
False                   # rosa nao está na lista 1

if rosa in lista1: # testa e imprime se rosa pertence a lista 1
    print("está na lista 1")
else:
    print("nao está")   

#################################  CONCATENACAO DE LISTA ######################

a = [1, 2]
b = [3, 4]
a + b = [1, 2, 3, 4]    #adiciona ao final da lista uma outra lista

x = [1, 2 , 3, "gato"]
y = x + [5]              # a soma só ocorre em formato de lista
y = [1, 2, 3, "gato", 5]

a = [1, 2]
a_triplicado = a * 3    # a multiplicação basta fazer normal
a_triplicado = [1, 2, 1, 2, 1, 2]


