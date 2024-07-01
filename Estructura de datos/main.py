notas =[
    ["calculo", 1.5, 2.5, 1.5],
    ["quimica", 1.5, 2.0, 5.5],
    ["calculo", 2.4, 2.0, 2.2],
    ["Logica", 1.5, 4.0, 4.5],
]


def calculo():
    global notas
    for nota in range(len(notas)) :
        materia = notas[nota][1]*0.3
        materia2 = notas[nota][2]*0.3
        materia3 = notas[nota][3]*0.4
        materiaFinal = materia + materia2  + materia3
        notas[nota].append(materiaFinal)
    print(notas)
    pass

calculo()


