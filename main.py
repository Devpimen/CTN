from App.routers import basedatos  as basedatos
from App.routers import basenotas  as basenotas
from App.routers import basecalculos  as basecalculos
from App.routers import graficos  as graficos
from pathlib import Path
import json
class Main:
    #constructor para el registro del sistema
    def __init__(self):
        self.mi_dict = {} #Diccionario para almacenar datos
        pass
    #Funcion segundo Menu
    def menu(self):
        while True:  # Mantener el bucle del menú
            print("===================================")
            print("Bienvenido al menu")
            print("1. Registrar sus materias")
            print("2. Ingresar notas")
            print("3. Eliminar")
            print("4. Ver almacenamiento")
            print("5. Guardar almacenamiento")
            print("6. Calculos estadisticos")
            print("7. Calcular porcentajes")
            print("8. Abrir nuevo archivo")
            print("9. Ver graficos") 
            print("10. Volver al menu de inicio")
            print("===================================")
            try:
                resp = int(input("Seleccione una opción: "))  # Pedir entrada del usuario
            except ValueError:
                print("El dato ingresado es inavalido, los datos disponibles son solo los numeros mostrados en panatalla")
                continue

            # ===================== OPCIÓN 1 =====================
            if resp == 1:
                self.mi_dict = basenotas.menu_assignment(self.mi_dict)

            # ===================== OPCIÓN 2 =====================
            elif resp == 2:
                self.mi_dict = basenotas.menu_cargarNotas(self.mi_dict)

            # ===================== OPCIÓN 3 =====================
            elif resp == 3:
                self.mi_dict = basenotas.Menu_delete_nota(self.mi_dict)

            # ===================== OPCIÓN 4 =====================
            elif resp == 4:
                self.mi_dict = basenotas.ver_dict(self.mi_dict)

            # ===================== OPCIÓN 5 =====================
            elif resp == 5:
                self.mi_dict = basedatos.guardar(self.mi_dict)

            # ===================== OPCIÓN 6 =====================
            elif resp == 6:
                self.mi_dict = basecalculos.estadistica(self.mi_dict)

            # ===================== OPCIÓN 7 =====================
            elif resp == 7:
                self.mi_dict = basecalculos.calcular_porcentaje_ponderado(self.mi_dict)

            # ===================== OPCIÓN 8 =====================
            elif resp == 8:
                self.cargar_datos()
            # ===================== OPCIÓN 9 =====================
            elif resp == 9:
                self.mi_dict = graficos.menu(self.mi_dict)
            # ===================== OPCIÓN 10 =====================
            elif resp == 10:
                print("Regresando al menu...")
                break
            # ===================== OPCIÓN Default =====================
            else:
                print("Opción no válida, intente nuevamente.❌")  
    #Funcion cargar de archivos JSON donde los datos estan almacenados en dict
    def cargar_datos(self):  
        while True:
            print("\nEsta funcion es para cargar los datos de su almacenamiento: ")
            print("📂 Directorio actual:")

            re = input("Desea cargar datos previos (si/no): ").strip().lower()

            # ===================== OPCIÓN SI =====================
            if re == "si":
                ruta = Path("save_Data/json")
                print("Los nombres de los archivos almacenados en la carpeta")
                #interar los archivos
                #for file in ruta:
                #    print(file)
                name = input("Ingrese el nombre del archivo a cargar: ")
                file = ruta / f"{name}.json" 
                try:
                    with open(file, "r") as archivo:
                        self.mi_dict = json.load(archivo)
                        print("✅ Archivo cargado exitosamente")
                        self.menu()
                        break

                except Exception as e:
                    print(f"❌ Error al leer el archivo: {e}")
                except ImportError as e:
                    print(f"❌ Error al importar el archivo: {e}")
                except ImportWarning as e:
                    print(f"❌ Error  peligro al importar el archivo: {e}")

            # ===================== OPCIÓN NO =====================
            elif re == "no":
                self.menu()
                break

            # ===================== DEFAULT =====================
            else:
                print("Opción no válida, intente nuevamente.❌")
    #Funcion de menu de inicio
    def pantalla(self):
        while True:
            print("===================================")
            print("   Bienvenido al Control de Notas")
            print("===================================")
            print("1. Cargar datos previos")
            print("2. Iniciar sin cargar datos")
            print("3. Cerar el programa")
            print("===================================")
            try:
                opcion = int(input("Selecciona una opción: "))
            except ValueError:
                print("El dato ingresado es inavalido, los datos disponibles son solo los numeros mostrados en panatalla")
                continue
            # ===================== OPCIÓN 1 =====================
            if opcion == 1:
                self.cargar_datos()
            # ===================== OPCIÓN 2 =====================
            elif opcion == 2:
                self.menu()
            # ===================== OPCIÓN 3 =====================
            elif opcion == 3:
                print("Cerrando el programa...")
                exit()
            # ===================== OPCIÓN Default =====================
            else:
                print("Opcion invalida. Asegurese de ingresar los datos correctos")
    
if __name__ == "__main__":
    app = Main()
    app.pantalla()
