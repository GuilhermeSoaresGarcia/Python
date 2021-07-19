print("Entrada de Dados:")
segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)
a = total_segs // 86400
segs_rest_dia = total_segs % 86400
b = segs_rest_dia // 3600
segs_rest_horas = total_segs % 3600
c = segs_rest_horas // 60
d = total_segs % 60
print("Saída de Dados:")
print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
