### Graficos ###
import matplotlib.pyplot as plt 
#grafico de barras del promedio de todas las materias
def grafico_barras_materias(mi_dict):
        print("cargando graficos.......")
        for materia, datos in mi_dict.items():
            stack_notas = [] #Almacenar todas las notas
            for pond, detalles in datos["ponderaciones"].items():
                nota = detalles["notas"]
                for valor in nota:
                    if  0 <= valor <= 100:
                        stack_notas.append(valor)
                        
            #Calcular el promedio de las notas
            promedio = sum(stack_notas) / len(stack_notas)     
            # graficar esta materia
            plt.bar(materia, promedio)
        # Crear gráfico
        plt.title("promedio de calificaciones por materia")
        plt.xlabel("materia")
        plt.ylabel("promedio")
        plt.ylim(0, 100)
        plt.grid(axis='y')
        plt.show()
        return mi_dict
#grafico de barras del promedio de notas de cada ponderacion
def grafico_barras_ponderacion(mi_dict):
        print("Cargando grafico.......")
        for materia, datos in mi_dict.items():
            #la materia
            for pond, detalles in datos["ponderaciones"].items():
                stack_notas = [] #almacenar las notas de una ponderacion
                notas_pond = detalles["notas"]
                #revisar las notas
                for nota in notas_pond:
                    if 0 <= nota <= 100:
                        stack_notas.append(nota)

                if len(stack_notas) == 0:
                    continue
                else:
                    promedio_pond = sum(stack_notas) / len(stack_notas)
                    plt.bar(pond, promedio_pond)
                
            # Crear gráfico
            plt.title(f"promedio de notas por ponderacion de  {materia} ")
            plt.xlabel("ponderacion")
            plt.ylabel("nota")
            plt.ylim(0, 100)
            plt.grid(axis='y')
            plt.show()
        return mi_dict
#grafico pastel de cada porcentaje de una materia
def grafico_pastel(mi_dict):
    print("Loading your pie chart.......")
    for materia, datos in mi_dict.items():
        #la materia
        stack_pond = []
        porcentaje_pond = []
        for pond, detalles in datos["ponderaciones"].items():
            stack_pond.append(pond)
            porcentaje_pond.append(detalles["porcentaje"])
            #revisar las notas
        # Crear gráfico    
        plt.pie(porcentaje_pond,labels=stack_pond,autopct="%1.1f%%",startangle=90)
        plt.title(f"Percentege by weightings {materia} ")
        plt.show()
    return mi_dict
"""
Nuevos graficos a realizar: 
    grafico de paleta pie chart para las ponderaciones de cada materia
    grafico de linea en funcion de notas en periodos de tiempo(Update del sistema)
    grafico de linea en funcion de ntas en funcion de semanas de diferentes materias o ponderaciones
"""

def menu(mi_dict):
    while True:
        print("\n Bienvenido a los graficos:")
        print("1. grafico de barras del promedio de todas las materias ")
        print("2. grafico de barras del promedio de notas de cada ponderacion")
        print("3. grafico pastel")
        print("4. salir")
        resp = input("Seleccione una opcion: ")
        if resp == "1": 
            mi_dict = grafico_barras_materias(mi_dict)
        elif resp == "2":
            mi_dict = grafico_barras_ponderacion(mi_dict)
        elif resp == "3":
            mi_dict = grafico_pastel(mi_dict)
        elif resp == "4":
            print("Leaving....")
            break
        else:
            print("Number input invalied❌")
    return mi_dict