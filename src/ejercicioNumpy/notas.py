import numpy as np 
import matplotlib.pyplot as plt
import csv

def get_moda(array):
    counter = {}
    for e in array:
        if e not in counter.keys():
            counter[e] = 1
        else:
            counter[e] += 1
    moda = 0
    moda_rep = 0
    for e, rep in counter.items():
        if rep > moda_rep:
            moda = e
    return moda


def get_stats_from_exam(col: np.array):
    moda = get_moda(col)
    mean = np.mean(col)
    max = np.max(col)
    return {
        "Media": mean,
        "Moda": moda,
        "Máximo": max
    }

cols = []
alumnos = []
tabla = []
with open("ejercicioNumpy/notas.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    for i,line in enumerate(reader):
        if i == 0:
            cols = line
            continue
        alumnos.append(line[0])
        info_alumno = np.array(line[1:], dtype=np.float64)
        info_alumno = np.nan_to_num(info_alumno)
        info_alumno = np.reshape(info_alumno, (1,5))

        if len(tabla) == 0:
            tabla = info_alumno
        else:
            tabla = np.concat((tabla, info_alumno))

print(tabla[0])

print(f"Estadísticas del Examen 1: {get_stats_from_exam(tabla[:,0])}")
print(f"Estadísticas del Examen 2: {get_stats_from_exam(tabla[:,1])}")
print(f"Estadísticas del Examen 3: {get_stats_from_exam(tabla[:,2])}")

print("-------------------MEDIAS-----------------------")

for i, name in enumerate(alumnos):
    mean = tabla[i, 0:3].mean()
    print(f"{name}: {mean:.2f}")

print("-------------------Asistencia-----------------------")

for i, name in enumerate(alumnos):
    if tabla[i, 4] < 0.8:
        print(f"{name} tiene una asistencia menor a 0.8")

fig, axis = plt.subplots()
axis.hist(tabla[:,0], 11)
axis.set_xlabel("Notas")
axis.set_ylabel("Nº Alumnos")
axis.set_title(f"Distribución de notas del {cols[1]}")

fig.savefig("ejercicioNumpy/figura.png")