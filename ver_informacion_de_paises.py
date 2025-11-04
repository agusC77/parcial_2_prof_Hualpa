import os
import csv

def eliminar_acentos(texto):
    acentos = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U"}
    return "".join(acentos.get(c, c) for c in texto)

def ver_informacion_pais(base_dir, texto_busqueda):
    print(f"=== Buscar información del país: {texto_busqueda.title()} ===")
    texto_normalizado = eliminar_acentos(texto_busqueda.lower())
    resultados = []
    def _buscar(dirpath):
        for entry in os.listdir(dirpath):
            ruta = os.path.join(dirpath, entry)
            if os.path.isdir(ruta):
                _buscar(ruta)
            elif entry.lower() == "info.csv":
                with open(ruta, "r", encoding="utf-8", newline="") as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        nombre = eliminar_acentos(row["País"].lower())
                        if texto_normalizado in nombre:
                            resultados.append(row)
    _buscar(base_dir)
    if not resultados:
        print("No se encontraron coincidencias.\n")
        return
    print(f"Se encontraron {len(resultados)} coincidencia(s):")
    for r in resultados:
        print(f"- {r['País'].title()} ({r['Continente'].title()}) → Población: {r['Población']}, Superficie: {r['Superficie']}")
    print()