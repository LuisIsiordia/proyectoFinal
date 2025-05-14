import utilerias
from datos import talleres
from datos import estudiantes
from datetime import date
inscripciones=[]

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
            #Mostrar taller aca
            break
        else:
            print("\nNo hay ningún taller con ese ID, seleccione otra opción")
    #Fecha de la inscripción
    fechaInscripcion = date.today().isoformat()
    #Selección de estudiante a inscribir
    while True:
            idEstudiante = int(input("\nIngrese el ID del estudiate que se va a inscribir: "))

            if any(idEstudiante == ID[0] for ID in estudiantes):
                #Mostrar estudiante aca con todos sus datos excepto el ID
                break
            else:
                print("\nNo hay ningún estudiante con ese ID, seleccione otra opción")
    ConfirmarRegistro = input("¿Confirmar el registro? (S/N): ").upper()
    utilerias.validarSiNo((ConfirmarRegistro))
    if ConfirmarRegistro == "S":
        inscripciones=[]
        if inscripciones:
            folio = inscripciones[-1]['folio'] + 1
        else:
            folio = 1
        inscripciones = [folio, fechaInscripcion, idEstudiante]
    if ConfirmarRegistro == "N":
        registroInscripcionTaller(resp)

    HacerOtroRegistro = input("¿Confirmar el registro? (S/N): ").upper()
    utilerias.validarSiNo((HacerOtroRegistro))
    if HacerOtroRegistro == "S":
        registroInscripcionTaller(resp)
    if HacerOtroRegistro == "N":
        menu.menu()

def cancelarInscripcionFolio():
    print("cancelar la inscripcion de un alumno mediante su folio")
    
def listadoInscripcionesTaller():
    print("listado de inscripciones en los talleres")