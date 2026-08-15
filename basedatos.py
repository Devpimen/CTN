import json
from pathlib import Path
#Save archive in format .doc
def save_word(mi_dict):
    name = input("Ingrese el nombre para guardar su archivo: ") + ".doc"
    ruta = Path("save_Data/doc")
    ruta_completa = ruta / f"{name}"
    # Verifica si la carpeta existe, si no la crea
    with open(ruta_completa, "w") as archivo:
        archivo.write("Bienvenido al almacenamiento de su control de notas \n")
        for materia, datos in mi_dict.items():
            archivo.write(f"--{materia.upper()}\n")
            for pond, detalles in datos["ponderaciones"].items():
                archivo.write(f"\t-{pond} {detalles['porcentaje']}%\n")
                archivo.write("\t"*2 + f"-Notas: {detalles['notas']}\n")
        print(f"\nDatos guardados correctamente en '{name}'.✅")
    return mi_dict
#Save archive in format .txt
def save_txt(mi_dict):
    name = input("Ingrese el nombre para guardar su archivo: ") + ".txt"
    ruta = Path("save_Data/txt")
    ruta_completa = ruta / f"{name}"
    with open(ruta_completa, "w") as archivo:
        archivo.write("Bienvenido al almacenamiento de su control de notas \n")
        for materia, datos in mi_dict.items():
            archivo.write(f"--{materia}\n")
            for pond, detalles in datos["ponderaciones"].items():
                archivo.write(f"\t-{pond} {detalles['porcentaje']}%\n")
                archivo.write("\t"*2 + f"-Notas: {detalles['notas']}\n")
        print(f"\nDatos guardados correctamente en '{name}'.✅")
    return mi_dict
#Save archive in format .json
def save_json(mi_dict):
    name = input("Ingrese el nombre del archivo: ") + ".json"
    ruta = Path("save_Data/json")
    ruta_completa = ruta / f"{name}"
    with open(ruta_completa, "w") as archivo:
        json.dump(mi_dict, archivo, indent=4)
    print(f"\nDatos guardados correctamente en '{name}'.✅")
    return mi_dict
#Menu save  archive in different format
def guardar(mi_dict):
    while True:
        print("Guardando el almacenamiento......")
        print("1. Guardar los datos en modo Documento de Word")
        print("2. Guardar los datos en un archivo de texto (.txt)")
        print("3. Guardar en formato JSON")
        print("4. Salir")
        try:
            resp = int(input("Seleccione una opción: "))

            # ===================== OPCIÓN 1 =====================
            if resp == 1:
                mi_dict = save_word(mi_dict)
            
            # ===================== OPCIÓN 2 =====================
            elif resp == 2:
                mi_dict = save_txt(mi_dict)
            
            # ===================== OPCIÓN 3 =====================
            elif resp == 3:
                mi_dict = save_json(mi_dict)
            
            # ===================== OPCIÓN 4 =====================
            elif resp == 4:
                print("Saliendo..............")
                break
            else:
                print("Número ingresado no válido❌, las opciones son 1, 2 o 3.")
                continue
        except ValueError:
            print("Entrada inválida. Ingrese un número entero (1, 2 o 3).")
    return mi_dict
