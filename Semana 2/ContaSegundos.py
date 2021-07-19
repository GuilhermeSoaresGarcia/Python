segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

#Dividir o input pelo total de segundos num dia e passar resto para variável "segs_rest_dia"
dias = total_segs // 86400
segs_rest_dia = total_segs % 86400

#Pegar o resto da variável "segs_rest_dia" e dividir pelo total de segundos numa hora, armazenando o resto na variável "segs_rest_horas"
horas = segs_rest_dia // 3600
segs_rest_horas = total_segs % 3600

#Pegar o resto da variável "segs_rest_horas" e dividir pelo total de segundos num minuto, armazenando o resto na variável "segs_rest_minutos"
minutos = segs_rest_horas // 60
segs_rest_minutos = total_segs % 60

print(dias, "dias, ", horas, "horas, ", minutos, "minutos e", segs_rest_minutos, "segundos.")
