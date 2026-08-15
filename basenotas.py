from fractions import Fraction
from pathlib import Path
import pandas as pd
import openpyxl
import os
#eliminar nota
def delete_qualification(mi_dict):
# Pedir la entrada de la materia
    #ver el contenido del dict
    mi_dict = ver_dict(mi_dict)
    resp_mat = input("\nIngrese el nombre de la materia: ").strip()
    if resp_mat in mi_dict:
        print("\nMateria encontrada✅")
        # Pedir la entrada de la ponderaccion
        resp_mat_pond = input("Ingrese el nombre de la ponderación a eliminar notas: ").strip()
        if resp_mat_pond in mi_dict[resp_mat]["ponderaciones"]:
            print("\nPonderación encontrada:✅")
            while True:
                # Acceder a la nota en la posición correspondiente
                can_notas = mi_dict[resp_mat]["ponderaciones"][resp_mat_pond]["notas"]
                # Mostrar las notas
                print(f"Las notas actuales en la ponderación {resp_mat_pond} son: ")
                print(f"{can_notas}")
                while True:
                    try:
                        nota_eliminar = float(input(" Ingrese la nota que quiere eliminar: "))
                        if 0 <= nota_eliminar <= 100:
                            continue
                        else:
                            print("❌ Error: El número debe estar entre 0 y 100.")
                        break
                    except ValueError:
                        print("El dato es invalido❌")
                        print("Solamente puede ingresar numero enteros(1,2,3,4,5...) y decimales(1.2, 8.9, 6.7, ...)")
                    if nota_eliminar in mi_dict[resp_mat]["ponderaciones"][resp_mat_pond]["notas"]:
                        mi_dict[resp_mat]["ponderaciones"][resp_mat_pond]["notas"].remove(nota_eliminar)
                        print(f"Nota {nota_eliminar} eliminada con éxito.✅")
                    else:
                        print(f"La nota {nota_eliminar} no se encuentra en la lista.")
                    des = input("Desea eliminar otra nota (si/no): ")
                    if des == "no".lower().strip():
                        break
                    elif des == "si".lower().strip():
                        continue
                    else:
                        print("Dato inválido❌, ingrese 'si' o 'no'.")
        else:
            print("\nPonderación no encontrada❌")
    else:
        print("\nMateria no encontrada❌")
    return mi_dict
#eliminar materia
def delete_assignment(mi_dict):
    # Mostrar las materias disponibles para eliminar
    print("Materias disponibles")
    for key,pond in mi_dict.keys():
        print(key.upper())
    while True:
        for materia, datos in mi_dict.items():
            print(f"-{materia.upper()}")
        re = input("Ingrese el nombre de la materia a eliminar: ")
        if re in mi_dict:
            print("\nMateria encontrada✅")
            del mi_dict[re]
            print(f"La materia {re} fue eliminada con exito✅")
        else:
            print(f"la materia {re} no existe, por favor ingrese los datos validos")
        desp =  input("Desea eliminar otra materia (si/no): ")
        if desp == "si".strip().lower():
            continue
        elif desp == "no".lower().strip():
            break
        else:
            print("dato invalido❌, por favor ingrese los datos validos ('si' / 'no')")
    return mi_dict
#input qualification
def input_qualification(mi_dict):
    mi_dict = ver_dict(mi_dict)
    nom_materia = str(input("Ingrese el nombre de la materia que desea ingresar notas: "))
    #verificar si la materia existe en el diccionario
    if nom_materia in mi_dict:
        print("\nMateria encontrada✅")
        name_pond = str(input("Ingrese el nombre de la ponderación donde almacenará notas: "))
        # Verificar si la ponderación existe en las ponderaciones de la materia
        if name_pond in mi_dict[nom_materia]["ponderaciones"]:
            print("\nPonderación encontrada✅")
            while True:
                try:
                    cant_notas = int(input(f"Ingrese la cantidad de notas que almacenara en {name_pond}: "))
                    if cant_notas <= 0:
                        print(f"las cantidad {cant_notas} no es valida")
                        continue # volver a pedir la cantidad
                    break # salir del bucle
                except ValueError:
                    print("El dato  solo puede ser entero (1,2,3,4,5), intentelo otra vez")
            for i in range(cant_notas):
                while True:
                    try:
                        no = input(f"Ingrese la nota {i + 1}: ")
                        # Validar si la nota ingresada es fraccion o no
                        if "/" in no:
                            # Convertir la fraccion a flotante
                            no = float(Fraction(no)) 
                        else:
                            no = float(Fraction(no))
                        if 0 <= no <= 100:
                            # Registrar la nota dentro del diccionario
                            mi_dict[nom_materia]["ponderaciones"][name_pond]["notas"].append(no)
                            print("\nNota registrada correctamente.✅") 
                            break
                        else:
                            print("❌ Error: El número debe estar entre 0 y 100.")                              
                    except ValueError:
                        print("El dato es inválido ❌...")
        else:
            print("\nPonderación no encontrada❌")
    else:
        print("\nMateria no encontrada❌")
    return mi_dict
#Loop para 
def loop_n(n,asunto):
    while True:
        try:
            cant_ponderaciones = int(input(f"Ingrese la cantidad de {asunto}: "))
            if cant_ponderaciones <= n:
                print(f"El número de {asunto} debe ser mayor a 0.")
                continue  # Vuelve a pedir el número
            return cant_ponderaciones                        
        except ValueError:
            print("Los valores permitidos son números enteros (1,2,3,4,5...)")
#Funcion Ingresar las materias
def add_assignment(mi_dict):
    cant_materias = loop_n(0,"materia")
    for i in range(cant_materias):
        #pedir el nombre de la materias 
        materia = str(input(f"Ingrese el nombre de la materia {i + 1}: ").strip().lower())                 
        #comprobar si existe la materia en mi dict
        if materia in mi_dict:
            print(f"La materia '{materia}' ya fue registrada.✅")
        else:
            #NO existe la materia entoces se crea la materia en el dict
            mi_dict[materia] = {"ponderaciones": {}}
            #validar la cantidad de ponderaciones en la materia
            cant_ponderaciones = loop_n(0,"ponderaciones")
            suma_ponrcentaje = 0
            for j in range(cant_ponderaciones):
                pond_name = str(input(f"Ingrese el nombre de la ponderación {j + 1} para '{materia}': ").strip())
                while True:
                    porcentaje = float(input(f"Ingrese el porcentaje de '{pond_name}' (solamente ingrese la cantidad sin el '%'  en rango de [0,100]): "))
                    if 0 < porcentaje <= 100:
                        break # romper el registro 
                    print("Porcentaje inválido❌. Intente de nuevo.")
                mi_dict[materia]["ponderaciones"][pond_name] = {
                "porcentaje":porcentaje, # guardar porcentaje
                "notas":[] } #guardar notas 
                #guardar los datos en el dict
                suma_ponrcentaje += porcentaje
            #comprobar que las ponderaciones sumen 100%
            if suma_ponrcentaje == 100:
                print(f"Materia '{materia}' registrada con éxito✅.\n")
            else:
                print(f"Error: La suma de los porcentajes para '{materia}' es {suma_ponrcentaje}%.")
                print("El registro de esta materia será eliminado❌. Por favor, inténtelo de nuevo.")
                del mi_dict[materia]
    return mi_dict
#menu assignment
def menu_assignment(mi_dict):
    while True:
        print("\nBienvenido al registro de materias:")
        print("1. Añadir materia")
        print("2. Salir")
        resp = input("Seleccione una opción: ")

        # ===================== OPCIÓN 1 =====================
        if resp == "1":
            print("Registro de materias:")
            mi_dict = add_assignment(mi_dict)

        # ===================== OPCIÓN 2 =====================
        elif resp == "2":
            print("Saliendo del registro de materias...")
            break
        else:
            print("Opción no válida❌. Intente de nuevo.")

    print("\nMaterias registradas:✅")
    for materia, datos in mi_dict.items():
        print(f"--{materia.upper()}")
        for pond, detalles in datos["ponderaciones"].items():
            print(f"\t-{pond} {detalles['porcentaje']}%")
            print("\t"*2 + f"-Notas: {detalles['notas']}")
    return mi_dict
#Funcion Ingresar notas en las materias manuelmente   
def Menu_ingresar_notas(mi_dict):
    # Función para ingresar las notas de las materias
    mi_dict = ver_dict(mi_dict)
    while True:
        print("1. Ingresar notas: ")
        print("2. Salir: ")
        while True:
            try:
                resp = int(input("Seleccione una opcion: "))
                break
            except ValueError:
                print("Tipo de dato invalido, asegurese de solo ingresar los numeros disponibles en pantalla")
                continue
        
        # ===================== OPCIÓN 1 =====================
        if resp == 1:
            mi_dict = input_qualification(mi_dict)

        # ===================== OPCIÓN 2 =====================        
        elif resp == 2:
            print("\nHasta luego crack")
            break
        else:
            print("\nOpcion invalida❌")

    
    return mi_dict 
#Funcion eliminar notas de las materias    
def Menu_delete_nota(mi_dict):
    # Función para eliminar notas o materias
    mi_dict = ver_dict(mi_dict)
    while True:
        print("\nOpciones:")
        print("1. Eliminar notas")
        print("2. Eliminar materias")
        print("3. Salir")
        while True:
            try:
                resp = int(input("\nSeleccione una opción:"))
                break
            except ValueError:
                print("El dato ingresado es invalido❌")
                continue 

        # ===================== OPCIÓN 1 =====================    
        if resp == 1:  # Eliminar notas
            mi_dict = delete_qualification(mi_dict)

        # ===================== OPCIÓN 2 =====================              
        elif resp == 2:  # Eliminar materias
            mi_dict = delete_assignment(mi_dict)

        # ===================== OPCIÓN 3 =====================            
        elif resp == 3:  # Salir
            print("\nHasta luego, crack")
            break
        else:
            print("Opción inválida❌")
    return mi_dict
#Funcion ver el almacenamiento del diccionario    
def ver_dict(mi_dict):
    # Función para ver el contenido del diccionario
    print("\nContenido de su almacenamiento:")
    for materia, datos in mi_dict.items():
        print(f"--{materia.upper()}")
        for pond, detalles in datos["ponderaciones"].items():
            print(f"\t-{pond} {detalles['porcentaje']}%")
            print("\t"*2 + f"-Notas: {detalles['notas']}")
    return mi_dict
#Funcion para abrir archivos en excel y sus datos
def cargar_dataExcel(mi_dict):
    while True:
        ruta = Path(r"D:\Proyectos_MC\Control_notas\Datos guardados\XLS")
        name_file = os.listdir(ruta)
        print("Los nombres de los archivos almacenados en la carpeta")
        for file in name_file:
            print(file)
        name_file = input("Ingrese el nombre del archivo Excel (sin .xlsx): ")
        ruta = Path(input("Ingrese la ruta donde  guardara el archivo: ").strip('"'))

        archivo = ruta / f"{name_file}.xlsx"

        if not archivo.is_file():
            print("❌ Archivo inválido")
            continue

        print("✅ Archivo cargado correctamente")
        df = pd.read_excel(archivo)
        print("Columnas detectadas:", list(df.columns))
        break

    print("\nModelos de carga:")
    print("1. Columna completa")
    print("2. Columna por rango de filas")
    print("3.Salir")

    op = input("Seleccione su opción: ")

    # ===================== OPCIÓN 1 =====================
    if op == "1":
        columnas = []

        while True:
            col = input("Ingrese el nombre de la columna: ").strip()

            if col not in df.columns:
                print("❌ Columna no existe")
                continue

            columnas.append(col)

            if input("¿Otra columna? (si/no): ").lower() != "si":
                break

        data = df[columnas]
        data = data.apply(pd.to_numeric, errors="coerce")

    # ===================== OPCIÓN 2 =====================
    elif op == "2":
        col = input("Ingrese el nombre de la columna: ").strip()

        if col not in df.columns:
            print("❌ Columna no existe")
            return mi_dict

        i = int(input("Fila inicial: "))
        f = int(input("Fila final: "))

        data = pd.to_numeric(df.loc[i:f, col], errors="coerce")

    # ===================== OPCIÓN 3 =====================
    elif op == "3":
        print("Saliendo.....")
        return mi_dict

    # ===================== OPCIÓN Default =====================
    else:
        print("❌ Opción inválida")
        return mi_dict

    # ===================== VALIDACIÓN NOTAS =====================
    if ((data < 0) | (data > 100)).any().any() if isinstance(data, pd.DataFrame) else ((data < 0) | (data > 100)).any():
        print("❌ Hay notas inválidas")
        return mi_dict

    # ===================== GUARDAR EN DICCIONARIO =====================
    name_materia = input("Ingrese el nombre de la materia: ")

    if name_materia not in mi_dict:
        print("❌ Materia no encontrada")
        return mi_dict

    name_pond = input("Ingrese el nombre de la ponderación: ")

    if name_pond not in mi_dict[name_materia]["ponderaciones"]:
        print("❌ Ponderación no encontrada")
        return mi_dict

    notas = data.values.flatten().tolist() if isinstance(data, pd.DataFrame) else data.tolist()

    mi_dict[name_materia]["ponderaciones"][name_pond]["notas"].extend(notas)

    print("✅ Notas registradas correctamente")
    return mi_dict
#Menu de forma de ingresar las notas
def menu_cargarNotas(mi_dict):
    print("Modelo para cargar las notas")
    print("1.Ingresar manualmente")
    print("2.Cargas notas de un archivo excel")
    print("3.Salir")
    op = int(input("Seleccie una opcion"))
    
    # ===================== OPCIÓN 1 =====================
    if op == 1:
        mi_dict = input_qualification(mi_dict)
        return mi_dict
    
    # ===================== OPCIÓN 2 =====================
    elif op == 2:
        mi_dict = cargar_dataExcel(mi_dict)
        return mi_dict
    
    # ===================== OPCIÓN 3 =====================
    elif op == 3:
        print("Saliendo....")
        return mi_dict
    else:
        print("Datos invalidos")
    return mi_dict