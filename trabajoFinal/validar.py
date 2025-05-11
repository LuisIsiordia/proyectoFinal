#Validación para agregar un taller
def validarAgregar(respuestaAgregar):
    while respuestaAgregar != "S" and respuestaAgregar != "N":
        print("Tipo de respues invalida escoja solo entre estos dos caracter ('S' o 'N')")
        respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
    return respuestaAgregar
def validarAgregar(respuestaAñadir):
    while respuestaAñadir != "S" and respuestaAñadir != "N":
        print("Tipo de respues invalida escoja solo entre estos dos caracter ('S' o 'N')")
        respuestaAñadir = input("¿Quiere añadir otro taller? (S/N): ").upper()
    return respuestaAñadir
