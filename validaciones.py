def numero_positivo():
    while True:
        valor = input("Ingrese un número: ").strip()
        if not valor:
            print("El campo no puede estar vacío.")
            continue
        try:
            num = float(valor)
            if num <= 0:
                print("Debe ingresar un número positivo.")
                continue
            return valor
        except ValueError:
            print("Error: ingrese un número válido (sin letras ni símbolos).")

def validar_texto():
    while True:
        texto = input("Ingrese texto: ").strip()
        if not texto:
            print("El campo no puede estar vacío.")
            continue
        if all(c.isalpha() or c.isspace() for c in texto):
            return texto
        print("El texto solo puede contener letras y espacios.")