from editar_archivo import leer_todos_los_paises_recursivo
from ver_informacion_de_paises import eliminar_acentos
from validar import validar_texto

#============================================================================================================================

def paises_continente(directorio_actual):
    print("=== Mostrar países por continente ===")
    print("Ingrese el continente del país que desee visualizar:")
    # El usuario ingresa el nombre del continente
    while True:
        continente = validar_texto().lower()
        continente = eliminar_acentos(continente)
        match continente:
            case "america":
                break
            case "africa":
                break
            case "asia":
                break
            case "oceania":
                break
            case "europa":
                break
            case _:
                print("Error el continente ingresado no existe")
                print()

    # Se almacena en la lista todos, varios diccionarios, que seran todos los países ingresados con su información
    todos = leer_todos_los_paises_recursivo(directorio_actual)
    
    # Se almacena en una lista que pertenezcan al continente que ingreso el usuario
    encontrados = [p for p in todos if eliminar_acentos(p["Continente"].lower()) == continente]

    # Si la lista esta vacía es porque no se encontraron países asociados a ese continente
    if not encontrados:
        print("No se encontraron países en ese continente.\n")
        return

    # Caso contrario muestra todos los países asociados a dicho continente
    print(f"Países del continente {continente.title()}:")
    for p in encontrados:
        print(f"- {p['País'].title()}")
    print()

#============================================================================================================================

def ordenar_alfabetico(directorio_datos):
    print("=== Mostrar todos los países en orden alfabético ===")
    # Se almacena en la lista todos, varios diccionarios, que seran todos los países ingresados con su información
    todos = leer_todos_los_paises_recursivo(directorio_datos)

    # Ordenamiento burbuja
    cantidad_paises = len(todos)
    for pasada in range(cantidad_paises):
        for indice_actual in range(0, cantidad_paises - pasada - 1):
            # Comparamos los nombres de los países en minúsculas para ignorar mayúsculas
            if todos[indice_actual]["País"].lower() > todos[indice_actual + 1]["País"].lower():
                # Intercambiar posiciones
                todos[indice_actual], todos[indice_actual + 1] = todos[indice_actual + 1], todos[indice_actual]
    
    # Mostrar los países ordenados
    for pais in todos:
        print(f"- {pais['País'].title()} ({pais['Continente'].title()})")
    
    print()

#============================================================================================================================

def estadisticas_pais(directorio_datos, pais_buscar):
    # Almacena todods los países en una lista de diccionarios
    todos = leer_todos_los_paises_recursivo(directorio_datos)

    # Recorre cada país, en caso de que el país coincida con el país buscado devuelve el valor de este y deja de buscar
    # En caso de no encontrar el país buscado retorna nada
    pais = next((p for p in todos if p["País"].lower() == pais_buscar.lower()), None)

    # Si no se encontro el páis le avisamos al usuario
    if not pais:
        print("País no encontrado.\n")
        return
    
    # Convierte los datos de poblacion y superficie a float para calcular la densidad de población
    # Si la superficie es 0 o hay algún error al convertir los datos, asigna densidad = 0
    try:
        pobl = float(pais["Población"])
        sup = float(pais["Superficie"])
        densidad = pobl / sup if sup != 0 else 0
        pobl = int(pobl)
    except:
        densidad = 0
    # Muestras las estadísticas del país ingresado
    print(f"=== Estadísticas del país: {pais_buscar.title()} ===")
    print(f"Población: {pobl:,}")
    print(f"Superficie: {sup:,}km2")
    print(f"Densidad: {densidad:.2f} habitantes por unidad de superficie.\n")
    print()

    #============================================================================================================================