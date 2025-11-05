from editar_archivo import agregar_paises, eliminar_pais, modificar_archivo, leer_todos_los_paises_recursivo
from validar import validar_texto
from ver_informacion_de_paises import ver_informacion_pais
from filtrar_los_paises import paises_continente, ordenar_alfabetico, estadisticas_pais
import os

# Define una variable con el nombre de un directorio/carpeta
DIRECTORIO_DATOS = "datos"

#============================================================================================================================

# Verifica si existe al menos un archivo info.csv en la carpeta de datos.
def hay_datos_creados(directorio):
    for ruta_actual, _, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.lower() == "info.csv":
                return True
    return False

#============================================================================================================================

if __name__ == "__main__":
    # Crea la carpeta datos si no existe, caso contrario exist_ok=True permite que no se genere un error
    os.makedirs(DIRECTORIO_DATOS, exist_ok=True)
    print("=== Sistema de gestión jerárquica de países ===")
    while True:
        print("============MENÚ==============")
        print(" 1) Agregar países")
        print(" 2) Buscar país por nombre")
        print(" 3) Filtrar países por continente")
        print(" 4) Ordenar países alfabéticamente")
        print(" 5) Mostrar estadísticas de un país")
        print(" 6) Editar información de un país")
        print(" 7) Eliminar país")
        print(" 8) Mostrar todos los países (lectura recursiva)")
        print(" 9) Salir")
        print("==============================")
        opcion = input("Seleccione una opción: ").strip()
        print()

        # Opciones que requieren que existan datos previamente
        opciones_requieren_datos = {"2", "3", "4", "5", "6", "7", "8"}
        # En cao de que no exista ningún archivo info.csv no podran ejecutarse estas opciones
        if opcion in opciones_requieren_datos and not hay_datos_creados(DIRECTORIO_DATOS):
            print("Primero debe agregar al menos un país (opción 1).\n")
            continue    

        match opcion:
            case "1":
                agregar_paises(DIRECTORIO_DATOS)
            case "2":
                    print("Buscar país por nombre:")
                    texto = validar_texto()
                    ver_informacion_pais(DIRECTORIO_DATOS, texto)
            case "3":
                print("Filtrar países por continente:")
                paises_continente(DIRECTORIO_DATOS)
            case "4":
                print("Mostrar todos los países ordenados alfabéticamente:")
                ordenar_alfabetico(DIRECTORIO_DATOS)
            case "5":
                print("Mostrar estadísticas de un país:")
                texto = validar_texto()
                estadisticas_pais(DIRECTORIO_DATOS, texto)
            case "6":
                print("Modificar datos de un país existente:")
                texto = validar_texto()
                modificar_archivo(DIRECTORIO_DATOS, texto)
            case "7":
                print("Eliminar un país:")
                texto = validar_texto()
                eliminar_pais(DIRECTORIO_DATOS, texto)
            case "8":
                print("Lectura recursiva de todos los países:")
                todos = leer_todos_los_paises_recursivo(DIRECTORIO_DATOS)
                for d in todos:
                    print(f"- {d['País']} ({d['Continente']}) - Población: {d['Población']} - Superficie: {d['Superficie']}")
            case "9":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida, ingrese un número entre 1 y 9.")