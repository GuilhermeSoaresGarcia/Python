import math
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = b ** 2 - 4 * a * c

#se delta igual a 0 = uma raiz real que é tal
if delta == 0:
    x = (-(b) + (math.sqrt(delta))) / (2 * a)
    print("A raiz desta equação é", x)
else:
#se delta menor 0 = não tem raizes reais
    if delta < 0:
        print("Delta não possui raíz(es) real(is)")
#se maior 0 = duas raízes reais tal e tal
    else:
        x1 = (-(b) + (math.sqrt(delta))) / (2 * a)
        x2 = (-(b) - (math.sqrt(delta))) / (2 * a)
        print("As raízes reais são: X1 =", x1, "e X2 =", x2)
