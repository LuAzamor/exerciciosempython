# tabuada mostrando a tabuada, a partir do que o usuário digita. Ex: tabuada de 7.

n = int(input ("Tabuada de: "))
x = 0

while x <= 9:
    x = x + 1
    print((x), "x", (n), "=", (n*x))