# tabuada, a partir do que o usuário digita. Ex: tabuada de 5.

n=int (input ("Tabuada de: "))
x= 1

while x<=10:
    print("%d" % x, "x", "%d" %n, "=", (n*x))
    x= x+1

