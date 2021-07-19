import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

if delta == 0:
    x = int((-(b) + (math.sqrt(delta))) / (2 * a))
    print("a raiz dupla desta equação é X", x)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        x1 = (-(b) + (math.sqrt(delta))) / (2 * a)
        x2 = (-(b) - (math.sqrt(delta))) / (2 * a)
        if(x1 < x2):
            print("as raízes da equação são", x1, "e", x2)
        else:
            print("as raízes da equação são", x2, "e", x1)
            