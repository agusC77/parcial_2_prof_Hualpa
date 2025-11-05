def numero_positivo():
    while True:
        valor = input("Ingrese un número: ").strip()
        if not valor:
            print("El campo no puede estar vacío.")
            print()
            continue
        try:
            num = float(valor)
            if num <= 0:
                print("Debe ingresar un número positivo.")
                print()
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número válido (sin letras ni símbolos).")

#=======================================================================================================================

def validar_texto():
    while True:
        texto = input("Ingrese texto: ").strip()
        if not texto:
            print("El campo no puede estar vacío.")
            continue
        if all(caracter.isalpha() or caracter.isspace() for caracter in texto):
            return texto
        print("El texto solo puede contener letras y espacios.")

#=======================================================================================================================

# Función para validar si el país ingresado existe en el archivo
def validar_pais(ruta_archivo, pais_agregar):
    import os
    import csv

    existe = False
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            diccionario = csv.DictReader(archivo)
            lista = list(diccionario)
        
        for pais in lista:
            if pais["País"] == pais_agregar:
                existe = True
                break
    
    return existe