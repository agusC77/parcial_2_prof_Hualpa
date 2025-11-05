import os
import csv

#============================================================================================================================

def eliminar_acentos(texto):
    acentos = {"á":"a","é":"e","í":"i","ó":"o","ú":"u","Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U"}
    # Recorre el texto carácter por carácter. Si alguna letra tiene acento,
    # la reemplaza por su versión sin acento. Si no tiene, la deja igual.
    # El método .join une los caracteres resultantes en una sola cadena.
    return "".join(acentos.get(caracter, caracter) for caracter in texto)

#============================================================================================================================

def ver_informacion_pais(directorio_raiz, texto_busqueda):
    print(f"=== Buscar información del país: {texto_busqueda.title()} ===")
    # Elimina los acentos del texto para normalizarlo.
    texto_normalizado = eliminar_acentos(texto_busqueda.lower())
    # Almacena los países que coinciden con el texto ingresado.
    coincidencias = []

    # Función interna recursiva para buscar dentro de subcarpetas.
    def _buscar(ruta_actual):
        # Recorre cada elemento del directorio que puede se una carpeta o archio.
        # os.listdir(ruta_actual) devuelve una lista con los nombres de todos los archivos y carpetas que hay dentro 
        # de la carpeta indicada por ruta_actual.
        for elemento in os.listdir(ruta_actual):
            ruta = os.path.join(ruta_actual, elemento)

            # Si el elemento es una carpeta, vuelve a llamar a _buscar dentro de ella
            if os.path.isdir(ruta):
                _buscar(ruta)
            
            # Si el elemento es un archivo llamado "info.csv"
            elif elemento.lower() == "info.csv":
                # Genera una lista de diccionario donde cada diccionario es un país con su información
                with open(ruta, "r", encoding="utf-8", newline="") as archivo:
                    diccionario = csv.DictReader(archivo)
                    lista = list(diccionario)

                    # Recorre cada fila (cada país) del archivo CSV
                    for pais in lista:
                        nombre_pais = eliminar_acentos(pais["País"].lower())
                        # Busqueda parcial ----> si el País comienza con el texto/letra que ingreso el usuario se añade a la lista
                        # Busqueda absoluta ---> Si el nombre del país es gual al nombre que ingreso el usuario el país se ingresa
                        # a la lista
                        if nombre_pais.startswith(texto_normalizado):
                            coincidencias.append(pais)
    
    # Inicia la búsqueda desde la carpeta raíz
    _buscar(directorio_raiz)

    # Si no se encontró nada, lo indica
    if not coincidencias:
        print("No se encontraron coincidencias.\n")
        return
    
    # Si se encontraron coincidencias, las muestra
    print(f"Se encontraron {len(coincidencias)} coincidencia(s):")
    for r in coincidencias:
        print(f"- {r['País'].title()} ({r['Continente'].title()}) → Población: {r['Población']}, Superficie: {r['Superficie']}")
    print()

    #============================================================================================================================