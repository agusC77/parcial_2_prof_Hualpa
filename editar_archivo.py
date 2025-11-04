import os
import csv
from validar import validar_texto, numero_positivo

ENCABEZADO = ["País", "Continente", "Población", "Superficie"]

def ruta_info(cont, pais):
    return os.path.join("data", cont.lower(), pais.lower(), "info.csv")

def crear_jerarquia_y_guardar(cont, pais, poblacion, superficie):
    print(f"Creando jerarquía para {pais.title()} en {cont.title()}...")
    cont_dir = os.path.join("data", cont.lower())
    pais_dir = os.path.join(cont_dir, pais.lower())
    os.makedirs(pais_dir, exist_ok=True)
    path = ruta_info(cont, pais)
    existe = os.path.exists(path)
    with open(path, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ENCABEZADO)
        if not existe:
            print("Creando nuevo archivo con encabezado.")
            writer.writeheader()
        writer.writerow({
            "País": pais,
            "Continente": cont,
            "Población": poblacion,
            "Superficie": superficie
        })
    print(f"Datos de {pais.title()} guardados correctamente en {path}.\n")

def agregar_paises(base_dir="data"):
    print("=== Agregar país ===")
    if not os.path.exists("paises.csv"):
        print("Error: No se encontró el archivo paises.csv.")
        return

    paises_base = {}
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

        if nombre_pais not in paises_base:
            print("El país no está en la base de datos. Intente nuevamente.")
            continue

        continente = paises_base[nombre_pais]
        print(f"Continente asignado automáticamente: {continente.title()}")

        print("Ingrese la población:")
        while True:
            poblacion = numero_positivo().strip()
            if poblacion.isdigit():
                break
            print("Ingrese un número entero positivo para población.")

        print("Ingrese la superficie:")
        while True:
            superficie = numero_positivo().strip()
            try:
                float(superficie)
                break
            except ValueError:
                print("Ingrese un número válido para superficie.")

        crear_jerarquia_y_guardar(continente, nombre_pais, poblacion, superficie)
        more = input("¿Desea agregar otro país? (1=Sí, 2=No): ").strip()
        if more != "1":
            print("Finalizando carga de países.\n")
            break

def eliminar_pais(base_dir, pais_a_eliminar):
    print(f"=== Eliminar país: {pais_a_eliminar.title()} ===")
    pais_a_eliminar = pais_a_eliminar.lower()
    encontrados = []
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

    if not os.path.exists(base_dir):
        print("No existe la carpeta base.")
        return
    _recorrer(base_dir)
    if not encontrados:
        print("País no encontrado.\n")
        return

    for ruta in encontrados:
        os.remove(ruta)
        print(f"Archivo eliminado: {ruta}")
        pais_dir = os.path.dirname(ruta)
        cont_dir = os.path.dirname(pais_dir)
        if not os.listdir(pais_dir):
            os.rmdir(pais_dir)
            print(f"Carpeta eliminada: {pais_dir}")
        if not os.listdir(cont_dir):
            os.rmdir(cont_dir)
            print(f"Carpeta eliminada: {cont_dir}")
    print("Eliminación completada.\n")

def modificar_archivo(base_dir, pais_modificar):
    print(f"=== Modificar datos del país: {pais_modificar.title()} ===")
    pais_modificar = pais_modificar.lower()
    encontrados = []
    def _buscar(dirpath):
        for entry in os.listdir(dirpath):
            ruta = os.path.join(dirpath, entry)
            if os.path.isdir(ruta):
                _buscar(ruta)
            elif entry.lower() == "info.csv":
                with open(ruta, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    rows = list(reader)
                    for row in rows:
                        if row.get("País", "").lower() == pais_modificar:
                            encontrados.append((ruta, rows))
                            return
    _buscar(base_dir)
    if not encontrados:
        print("El país no se encontró.")
        return

    ruta, rows = encontrados[0]
    print(f"Archivo encontrado: {ruta}")
    print("¿Qué desea modificar?")
    print("1) Población")
    print("2) Superficie")
    print("3) Ambos")
    opcion = input("Seleccione una opción: ").strip()

    if opcion in ["1", "3"]:
        print("Ingrese nueva población:")
        poblacion = numero_positivo().strip()
        for r in rows:
            if r["País"].lower() == pais_modificar:
                r["Población"] = poblacion
    if opcion in ["2", "3"]:
        print("Ingrese nueva superficie:")
        superficie = numero_positivo().strip()
        for r in rows:
            if r["País"].lower() == pais_modificar:
                r["Superficie"] = superficie

    with open(ruta, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=ENCABEZADO)
        writer.writeheader()
        writer.writerows(rows)
    print("Datos modificados correctamente.\n")

def leer_todos_los_paises_recursivo(base_dir):
    print("=== Lectura recursiva de todos los países ===")
    resultados = []
    def _leer(dirpath):
        for entry in os.listdir(dirpath):
            ruta = os.path.join(dirpath, entry)
            if os.path.isdir(ruta):
                print(f"Entrando en carpeta: {ruta}")
                _leer(ruta)
            elif entry.lower() == "info.csv":
                print(f"Leyendo archivo: {ruta}")
                with open(ruta, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        resultados.append(row)
    _leer(base_dir)
    print(f"Lectura completa. Se encontraron {len(resultados)} registros.\n")
    return resultados