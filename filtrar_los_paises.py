from editar_archivo import leer_todos_los_paises_recursivo
from ver_informacion_de_paises import eliminar_acentos

def paises_continente(base_dir):
    print("=== Mostrar países por continente ===")
    continente = input("Ingrese un continente: ").strip().lower()
    todos = leer_todos_los_paises_recursivo(base_dir)
    encontrados = [p for p in todos if eliminar_acentos(p["Continente"].lower()) == eliminar_acentos(continente)]
    if not encontrados:
        print("No se encontraron países para ese continente.\n")
        return
    print(f"Países del continente {continente.title()}:")
    for p in encontrados:
        print(f"- {p['País'].title()}")
    print()

def ordenar_alfabetico(base_dir):
    print("=== Mostrar todos los países en orden alfabético ===")
    todos = leer_todos_los_paises_recursivo(base_dir)
    ordenados = sorted(todos, key=lambda x: x["País"].lower())
    for p in ordenados:
        print(f"- {p['País'].title()} ({p['Continente'].title()})")
    print()

def estadisticas_pais(base_dir, pais_buscar):
    print(f"=== Estadísticas del país: {pais_buscar.title()} ===")
    todos = leer_todos_los_paises_recursivo(base_dir)
    pais = next((p for p in todos if p["País"].lower() == pais_buscar.lower()), None)
    if not pais:
        print("País no encontrado.\n")
        return
    try:
        pobl = float(pais["Población"])
        sup = float(pais["Superficie"])
        densidad = pobl / sup if sup != 0 else 0
    except:
        densidad = 0
    print(f"Población: {pobl:,}")
    print(f"Superficie: {sup:,}")
    print(f"Densidad: {densidad:.2f} habitantes por unidad de superficie.\n")