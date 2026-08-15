import statistics as sta
from scipy.stats import kurtosis, skew

#Funcion de calculos estadisticos en las materias registradas
def estadistica(mi_dict):
    print("\nCálculos estadísticos se realizarán......")
    todas_las_notas = []
    for materia, datos in mi_dict.items():
        for ponderacion, detalles in datos["ponderaciones"].items():
            todas_las_notas.extend(detalles["notas"])  # Agregamos correctamente todas las notas
    # Validamos si hay notas antes de hacer cálculos estadísticos
    if todas_las_notas:
        print("Medidas de tendencia central")
        print("\t-Media:", sta.mean(todas_las_notas))
        print("\t-Mediana:", sta.median(todas_las_notas))
        print("\t-Moda:", sta.mode(todas_las_notas))
        cantidad = len(todas_las_notas)
        if cantidad >= 2:
            print("Medidas de dispersión")
            print("\t-Desviación estándar muestral:", sta.stdev(todas_las_notas))
            print("\t-Varianza:", sta.variance(todas_las_notas))

        vmax = max(todas_las_notas)
        vmin = min(todas_las_notas)
        print("\t-Rango:", vmax - vmin)
        if cantidad >= 4:
            print("Medidas de forma")
            curtosis = kurtosis(todas_las_notas)
            asimetria = skew(todas_las_notas)
            print(f"\tCurtosis: {curtosis}")
            print(f"\tAsimetría: {asimetria}")
    else:
        print("\t-No hay notas registradas.❌")
    return mi_dict
#Funcion para calcular los porcentajes registradis de las nostas almacenadas
def calcular_porcentaje_ponderado(mi_dict):
        print("Bienvenido al cálculo de las ponderaciones por materia")
        
        for materia, datos in mi_dict.items():
            print(f"\nMateria: {materia.upper()}")
            total_porcentaje = 0
            nota_ponderada_total = 0

            for ponderacion, detalles in datos["ponderaciones"].items():
                porcentaje = detalles["porcentaje"]
                notas = detalles["notas"]
                cant = len(notas)

                if cant > 0:
                    promedio_notas = sum(notas) / cant
                    nota_ponderada = (promedio_notas * porcentaje) / 100
                    nota_ponderada_total += nota_ponderada
                    total_porcentaje += porcentaje

                    print(f"\tPonderación: {ponderacion}")
                    print(f"\tPromedio de notas: {round(promedio_notas, 2)}")
                    print(f"\tNota ponderada: {round(nota_ponderada, 2)} (de {porcentaje}%)")

            if total_porcentaje == 100:
                print(f"\nTotal nota ponderada para {materia}: {round(nota_ponderada_total, 2)}%")

                if nota_ponderada_total >= 91:
                    print("Su calificación es una A")
                elif nota_ponderada_total >= 81:
                    print("Su calificación es una B")
                elif nota_ponderada_total >= 71:
                    print("Su calificación es una C")
                elif nota_ponderada_total >= 61:
                    print("Su calificación es una D")
                else:
                    print("Su calificación es una F")

            else:
                print(f"\n¡Advertencia! Los porcentajes de las ponderaciones no suman 100% para {materia}.")
                print(f"Su porcentaje actual sin el semestral es: {round(nota_ponderada_total, 2)}%")
                print("\nSe mostrarán las letras que aún puede conseguir:")

                valor_semestral = 100 - total_porcentaje  
                valor_A = ((91 - nota_ponderada_total) / valor_semestral) * 100
                valor_B = ((81 - nota_ponderada_total) / valor_semestral) * 100
                valor_C = ((71 - nota_ponderada_total) / valor_semestral) * 100
                valor_D = ((61 - nota_ponderada_total) / valor_semestral) * 100
                
                posible_letra = False  # Bandera para determinar si alguna letra es alcanzable

                if valor_A <= 100:
                    print(f"✅ Es posible obtener la A si obtiene al menos {round(valor_A, 2)} en el semestral.")
                    posible_letra = True
                if valor_B <= 100:
                    print(f"✅ Es posible obtener la B si obtiene al menos {round(valor_B, 2)} en el semestral.")
                    posible_letra = True
                if valor_C <= 100:
                    print(f"✅ Es posible obtener la C si obtiene al menos {round(valor_C, 2)} en el semestral.")
                    posible_letra = True
                if valor_D <= 100:
                    print(f"✅ Es posible obtener la D si obtiene al menos {round(valor_D, 2)} en el semestral.")
                    posible_letra = True

                if not posible_letra:
                    print("❌ Solo puede obtener la F. 😞")

        return mi_dict