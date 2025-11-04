from edicion_archivo import agregar_paises, eliminar_pais, modificar_archivo, leer_todos_los_paises_recursivo
from validaciones import validar_texto
from ver_informacion_paises import ver_informacion_pais
from filtrar_paises import paises_continente, ordenar_alfabetico, estadisticas_pais
import os

DATA_DIR = "data"

if __name__ == "__main__":
    os.makedirs(DATA_DIR, exist_ok=True)
    print("=== Sistema de gestión jerárquica de países ===")
    while True:
        print("==============================")
        print("            MENÚ")
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

        match opcion:
            case "1":
                agregar_paises(DATA_DIR)
            case "2":
                print("Buscar país por nombre:")
                texto = validar_texto()
                ver_informacion_pais(DATA_DIR, texto)
            case "3":
                print("Filtrar países por continente:")
                paises_continente(DATA_DIR)
            case "4":
                print("Mostrar todos los países ordenados alfabéticamente:")
                ordenar_alfabetico(DATA_DIR)
            case "5":
                print("Mostrar estadísticas de un país:")
                texto = validar_texto()
                estadisticas_pais(DATA_DIR, texto)
            case "6":
                print("Modificar datos de un país existente:")
                texto = validar_texto()
                modificar_archivo(DATA_DIR, texto)
            case "7":
                print("Eliminar un país:")
                texto = validar_texto()
                eliminar_pais(DATA_DIR, texto)
            case "8":
                print("Lectura recursiva de todos los países:")
                todos = leer_todos_los_paises_recursivo(DATA_DIR)
                for d in todos:
                    print(f"- {d['País']} ({d['Continente']}) - Población: {d['Población']} - Superficie: {d['Superficie']}")
            case "9":
                print("Saliendo del sistema. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida, ingrese un número entre 1 y 9.")