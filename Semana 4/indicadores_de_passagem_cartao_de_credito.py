meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaoLido = 1
encontreiMeuCartaoNalista = False

while cartaoLido != 0 and not encontreiMeuCartaoNalista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao:
        encontreiMeuCartaoNalista = True

if encontreiMeuCartaoNalista:
    print("Eba, meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá!")
