import os
import csv
import shutil
from validar import *

ENCABEZADO = ["País", "Continente", "Población", "Superficie"]

#==========================================================================================================================
# Función que devuelve la ruta completa del archivo
def ruta_info(cont, pais):
    # Retorna (datos/continente/pais/info.csv)
    return os.path.join("datos", cont.lower(), pais.lower(), "info.csv")

#==========================================================================================================================

def crear_jerarquia_y_guardar(cont, pais, poblacion, superficie):
    print(f"Creando jerarquía para {pais.title()} en {cont.title()}...")
    # Almacena en directorio_continente la siguiente ruta "datos/continente_dle_país_elejido"
    directorio_continente = os.path.join("datos", cont.lower())
    # Almacena en directorio_pais la siguiente ruta "datos/nombre_continente/pais_ingresado"
    directorio_pais = os.path.join(directorio_continente, pais.lower())
    # Crea las carpetas indicadas en la ruta (datos/america/argentina) si no existen.
    # Si ya existen, no hace nada por el parámetro (exist_ok=True).
    os.makedirs(directorio_pais, exist_ok=True)
    # En la variable ruta_completa almacena la ruta completa hacia el archivo.
    ruta_completa = ruta_info(cont, pais)
    # Verifica si el archivo existe en el sistema
    existe = os.path.exists(ruta_completa)
    # Valida que no se haya ingresado antes.
    ya_ingresado = validar_pais(ruta_completa, pais)

    if ya_ingresado:
        return True
    else:
        # Agrega un país con su información al archivo
        with open(ruta_completa, "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=ENCABEZADO)
            # Si el archivo no existe lo crea, y agrega el encabezado
            if not existe:
                print("Creando nuevo archivo con encabezado.")
                writer.writeheader()
            # Agrega una linea con la información del país
            writer.writerow({"País": pais, "Continente": cont, "Población": poblacion, "Superficie": superficie})
        
        print(f"Datos de {pais.title()} guardados correctamente en {ruta_completa}.\n")

#==========================================================================================================================

def agregar_paises(base_dir="data"):
    print("=== Agregar país ===")
    if not os.path.exists("paises.csv"):
        print("Error: No se encontró el archivo paises.csv.")
        return

    # Variable que almacenara un país como key y el continente al que pertenece como value
    paises_base = {}
    # Recorre linea por linea el archivo, cada linea se transforma en una lista para poder obtener el nombre del país 
    # y su continente por separado. Esto permitira agregar al diccionario paises_base una key que sera el nombre del 
    # país y un value que sera el continente al que pertenece.
    with open("paises.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 2:
                nombre = partes[0].strip().lower()
                continente = partes[1].strip().lower()
                paises_base[nombre] = continente

    while True:
        print("Ingrese el nombre del país:")
        nombre_pais = validar_texto().strip().lower()
        print()

        if nombre_pais not in paises_base:
            print("El país no está en la base de datos. Intente nuevamente.")
            print()
            continue

        # A continente se le asigna el valor asociado a la key de paises_base
        continente = paises_base[nombre_pais]
        print(f"Continente asignado automáticamente: {continente.title()}")
        print()

        print("Ingrese la población:")
        while True:
            poblacion = numero_positivo()
            print()
            if poblacion.isdigit():
                break
            print("Ingrese un número entero positivo para población.")

        print("Ingrese la superficie:")
        while True:
            superficie = numero_positivo()
            print()
            try:
                float(superficie)
                break
            except ValueError:
                print("Ingrese un número válido para superficie.")

        # Agrega la información del país a un archivo en caso de que no haya sido ingresado, caso contrario
        # Le informamos al usuario que el país ya habia sido ingresado y le pedimos que ingrese otro
        if crear_jerarquia_y_guardar(continente, nombre_pais, poblacion, superficie):
            print(f"Error, el país {nombre_pais} ya se ha ingresado. Por favor intente con otro \n")
            continue
        
        opcion = ""
        while opcion not in ["1", "2"]:
            opcion = input("¿Desea agregar otro país? (1=Sí, 2=No): ").strip()
            print()
            if  not opcion in ["1", "2"]:
                print("Error, porfavor ingrse un úmero entre 1 y 2")
        if opcion == "2":
            print("Finalizando carga de países.\n")
            print()
            break

#==========================================================================================================================

# Función para eliminar un país del archivo
import os
import csv
import shutil

def eliminar_pais(base_dir, pais_a_eliminar):
    print(f"=== Eliminar país: {pais_a_eliminar.title()} ===")
    pais_a_eliminar = pais_a_eliminar.lower()
    encontrados = []

    # Recorre las carpetas buscando archivos info.csv
    def _recorrer(dirpath):
        for entry in os.listdir(dirpath):
            ruta = os.path.join(dirpath, entry)
            if os.path.isdir(ruta):
                _recorrer(ruta)
            elif os.path.isfile(ruta) and entry.lower() == "info.csv":
                with open(ruta, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        if row.get("País", "").lower() == pais_a_eliminar:
                            encontrados.append(ruta)

    # Verifica que la carpeta base exista
    if not os.path.exists(base_dir):
        print(" No existe la carpeta base.")
        return

    _recorrer(base_dir)

    # Si no se encuentra el país
    if not encontrados:
        print(" País no encontrado.\n")
        return

    # Elimina los archivos y carpetas relacionadas
    for ruta in encontrados:
        try:
            os.remove(ruta)
            print(f"🗑️ Archivo eliminado: {ruta}")
            pais_dir = os.path.dirname(ruta)
            cont_dir = os.path.dirname(pais_dir)

            # Borra la carpeta del país
            if os.path.exists(pais_dir):
                shutil.rmtree(pais_dir, ignore_errors=True)
                print(f"📁 Carpeta del país eliminada: {pais_dir}")

            # Borra la carpeta del continente si queda vacía
            if os.path.exists(cont_dir) and not os.listdir(cont_dir):
                os.rmdir(cont_dir)
                print(f"🌍 Carpeta del continente eliminada: {cont_dir}")

        except Exception as e:
            print(f"⚠️ Error al eliminar {ruta}: {e}")

    print("✅ Eliminación completada.\n")


#============================================================================================================================

def modificar_archivo(directorio_datos, pais_modificar):
    print(f"=== Modificar datos del país: {pais_modificar.title()} ===")
    pais_modificar = pais_modificar.lower()
    encontrados = []
    # Función interna recursiva para buscar dentro de subcarpetas.
    def _buscar(ruta_actual):
        # Recorre cada elemento de la carpeta indicada en ruta_actual.
        for elemento in os.listdir(ruta_actual):
            # Genera una nueva ruta con uno de los elemento del archivo
            ruta = os.path.join(ruta_actual, elemento)
            # Si la ruta generada es para abrir un archivo llama nuevamente a la función
            if os.path.isdir(ruta):
                _buscar(ruta)
            # Si la ruta te lleva a un archivo llamado info.csv
            elif elemento.lower() == "info.csv":
                # Abre el archivo y genera una lista de diccionarios donde cada diccionario es un país con su información
                with open(ruta, "r", encoding="utf-8", newline="") as archivo:
                    diccionario = csv.DictReader(archivo)
                    lista = list(diccionario)
                    for fila in lista:
                        if fila.get("País", "").lower() == pais_modificar:
                            encontrados.append((ruta, lista))
                            return
    _buscar(directorio_datos)
    if not encontrados:
        print("El país no se encontró.")
        return

# Se le asigna a ruta la ruta del archivo y a linea_archivo la lista de diccionarios
    ruta, linea_archivo = encontrados[0]
    while True:
        print(f"Archivo encontrado: {ruta}")
        print("¿Qué desea modificar?")
        print("1) Población")
        print("2) Superficie")
        print("3) Ambos")
        opcion = input("Seleccione una opción: ").strip()
        if opcion not in ["1", "2", "3"]:
            print("Por favor ingrese un número entre 1 y 3")
            continue
        break

    # Le pide al usuario que ingrese la población del país
    if opcion in ["1", "3"]:
        print("Ingrese nueva población:")
        poblacion = numero_positivo().strip()
        for pais in linea_archivo:
            if pais["País"].lower() == pais_modificar:
                pais["Población"] = poblacion
    # Le pide al usuario que ingrese la superficie
    if opcion in ["2", "3"]:
        print("Ingrese nueva superficie:")
        superficie = numero_positivo().strip()
        for pais in linea_archivo:
            if pais["País"].lower() == pais_modificar:
                pais["Superficie"] = superficie

    # Sobre escrive el archivo con los valores modificados
    with open(ruta, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ENCABEZADO)
        writer.writeheader()
        writer.writerows(linea_archivo)
    print("Datos modificados correctamente.\n")

#============================================================================================================================

# Función que almacenara todos los países en una lista
def leer_todos_los_paises_recursivo(directorio_actual):
    print("=== Lectura recursiva de todos los países ===")
    resultados = []
    # Función interna recursiva para buscar dentro de subcarpetas.
    def _leer(ruta_actual):
        # Recorre cada elemento de la carpeta indicada en ruta_actual.
        # Recorrera todos los elementosde de la carpeta datos  para almacenar 
        # todos los países de todos los archivos info.csv en una lista.
        for elemento in os.listdir(ruta_actual):
            # Genera una nueva ruta con uno de los elementos de la carpeta
            ruta = os.path.join(ruta_actual, elemento)

            # Si el elemento es una carpeta, vuelve a llamar a _buscar dentro de ella
            if os.path.isdir(ruta):
                print(f"Entrando en carpeta: {ruta}")
                _leer(ruta)
            
            # Si el elemento es un archivo llamado "info.csv"
            elif elemento.lower() == "info.csv":
                print(f"Leyendo archivo: {ruta}")
                # Genera una lista de diccionario donde cada diccionario es un país con su información
                with open(ruta, "r", encoding="utf-8", newline="") as archivo:
                    diccionario = csv.DictReader(archivo)
                    lista = list(diccionario)

                    # Almecena el país en una lista
                    for pais in lista:
                        resultados.append(pais)
    
    # Inicia la búsqueda desde la carpeta raíz
    _leer(directorio_actual)
    print(f"Lectura completa. Se encontraron {len(resultados)} registros.\n")
    return resultados

#============================================================================================================================
