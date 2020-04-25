import math

x1= float (input("Digite o ponto x1: "))
y1= float (input("Digite o ponto y1: "))
x2= float (input("Digite o ponto x2: "))
y2= float (input("Digite o ponto y2: "))

distancia = math.sqrt (abs (x1-x2**2) + abs (1-y2**2))

if distancia >= 10:
    print("longe")
else:
    print("perto")