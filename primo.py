def éprimo (k):
    div = 2
    while k % div != 0 and div <= k:   
        div = div + 1
        if k % div == 0:
            k = k - 1
        else:
            print (k)



numero = int(input("Digite um numero inteiro: "))



def maior_primo (éprimo):
    while numero > 0:
        if éprimo (numero) != True:
            numero = numero -1
        else:
            maior_primo = numero
            print (maior_primo)