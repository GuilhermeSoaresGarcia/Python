#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd';

# Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input("Digite seu nome (mínimo 3 caracteres): ")
verificaNome = len(nome) > 3

while verificaNome == False:
    nome = input("Nome deve ter pelo menos 3 caracteres: ")
    verificaNome = len(nome) > 3

idade = int(input("Digite a sua idade (número entre 0 e 150): "))
verificaIdade = idade > 0 and idade < 150

while verificaIdade == False:
    idade = int(input("Número deve ser entre 0 e 150: "))
    verificaIdade = idade > 0 and idade < 150

salario = int(input("Digite seu salário atual (deve ser maior do que 0): "))
verificaSalario = salario > 0

while verificaSalario == False:
    salario = int(input("Salário deve ser maior do que 0: "))
    verificaSalario = salario > 0

sexo = input("Digite seu sexo ('f' para 'feminino' ou 'm' para 'masculino'): ")
verificaSexo = sexo == "f" or sexo == "m" 

while verificaSexo == False:
    sexo = input("Deve ser 'f' ou 'm': ")
    verificaSexo = sexo == "f" or sexo == "m" 

estadoCivil = input("Digite seu estado civil ('s' para 'solteiro(a)', 'c' para 'casado(a)', 'v' para 'viúvo(a)' e 'd' para 'divorciado(a)': ")
verificaEstadoCivil = estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d"

while verificaEstadoCivil == False:
    estadoCivil = input("Deve ser 's', 'c', 'v' ou 'd': ")
    verificaEstadoCivil = estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d"

print()    
print("Nome:", nome)
print("Idade:", idade, "anos")
print("Salário: R$", salario)
if sexo == "f":
    print("Sexo: Feminino")    
else:
    print("Sexo: Masculino")

if estadoCivil == "s" and sexo == "f":
    print("Estado civil: Solteira")
elif estadoCivil == "s" and sexo == "m":
    print("Estado civil: Solteiro")
elif estadoCivil == "c" and sexo == "f":
    print("Estado civil: Casada")
elif estadoCivil == "c" and sexo == "m":
    print("Estado civil: Casado")
elif estadoCivil == "v" and sexo == "f":
    print("Estado civil: Viúva")
elif estadoCivil == "v" and sexo == "m":
    print("Estado civil: Viúvo")
elif estadoCivil == "d" and sexo == "f":
    print("Estado civil: Divorciada")
else:
    print("Estado civil: Divorciado")
