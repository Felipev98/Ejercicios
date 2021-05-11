# 3) Al terminar un día en un colegio secundario se hace una estadística de faltas sabiendo
# de cada curso:
#     Curso (1-5)
#     Presentes
#     Ausentes
# Calcular
#     Por cada curso el porcentaje de presentes sobre el total
#     Cantidad de ausentes en el colegio
#     Curso con mayor cantidad de ausente
curso = 0
numeroAusentes = []
porcentajePresentes = []
totalAlumnos = int(input('Ingrese el total de alumnos por curso: '))
while curso !=5:
    ausentes = int(input('Agregue la cantidad de alumnos ausentes del día de hoy: '))
    alumnos = numeroAusentes.append(ausentes)
    print(numeroAusentes)
    alumnosPresentes = (totalAlumnos - ausentes) 
    porcentajeAlumnos = (alumnosPresentes/totalAlumnos)*100
    alumnosPorcentajeTotal = porcentajePresentes.append(porcentajeAlumnos)
    print('El porcentaje de alumnos presentes es: ',porcentajePresentes)
    curso+=1

print('El curso con mayor cantidad de ausentes fue: ',max(numeroAusentes))