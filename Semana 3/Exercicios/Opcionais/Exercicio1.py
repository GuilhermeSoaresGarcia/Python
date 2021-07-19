import math
x1 = int(input("Digite o X do ponto 1: "))
y1 = int(input("Digite o Y do ponto 1: "))
x2 = int(input("Digite o X do ponto 2: "))
y2 = int(input("Digite o Y do ponto 2: "))

d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

if(d >=10):
    print("longe")
else:
    print("perto")
