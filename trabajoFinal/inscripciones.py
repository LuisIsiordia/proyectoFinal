import utilerias
from datos import talleres, estudiantes, inscripcionesTupla
from datetime import date

def registroInscripcionTaller(resp):
    utilerias.limpiarPantalla()
    utilerias.ordenamientoTalleres(resp)
    #Selección de taller
    while True:
        idTaller = int(input("\nIngrese el ID del taller al que quiere hacer una inscripción"
                             "\nEn caso de querer cancelar la inscripción ingrese un valor negativo (-1,-2, etc): "))
        if idTaller < 0:
            import menu
            menu.menu()
        if idTaller in talleres:
            utilerias.mostrarTaller(idTaller)
            break
        else:
            print("\nNo hay ningún taller con ese ID, seleccione otra opción")
    #Fecha de la inscripción
    fechaInscripcion = date.today().isoformat()
    #Selección de estudiante a inscribir
    while True:
            idEstudiante = int(input("\nIngrese el ID del estudiate que se va a inscribir: "))

            if any(idEstudiante == ID[0] for ID in estudiantes):

                break
            else:
                print("\nNo hay ningún estudiante con ese ID, seleccione otra opción")
    ConfirmarRegistro = input("¿Confirmar el registro? (S/N): ").upper()
    utilerias.validarSiNo((ConfirmarRegistro))
    if ConfirmarRegistro == "S":
        if inscripcionesTupla:
            folio = inscripcionesTupla[-1][0] + 1
        else:
            folio = 1
        inscripcion = (folio, fechaInscripcion, idEstudiante, idTaller)
        inscripcionesTupla.append(inscripcion)
    utilerias.mostrarTaller(idTaller)
    
    if ConfirmarRegistro == "N":
        HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()

    HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()
    while HacerOtroRegistro != "S" and HacerOtroRegistro != "N":
        print("Tipo de respuesta invalida escoja solo entre estos dos caracter ('S' o 'N')")
        HacerOtroRegistro = input("¿Continuar con otra inscripción a un taller (S/N)?: ").upper()
    if HacerOtroRegistro == "S":
        registroInscripcionTaller(resp)
    if HacerOtroRegistro == "N":
        import menu
        menu.menu()

def cancelarInscripcionFolio():
    folio = int(input("Seleccione un folio de una inscripción a cancelar: "))
    
    inscripcionesTupla = [i for i in inscripcionesTupla if i[0] != folio]
    
def cancelarInscripcionIDtaller(idtaller):
    global inscripcionesTupla
    inscripcionesTupla = [i for i in inscripcionesTupla if i[3] != idtaller]

def listadoInscripcionesTaller():
 print(inscripcionesTupla)

