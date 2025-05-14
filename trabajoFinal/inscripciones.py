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
    if inscripciones:
        siguiente_folio = inscripciones[-1]['folio'] + 1
    else:
        siguiente_folio = 1
    #Fecha de la inscripción
    fechaInscripcion = date.today().isoformat()
    #Selección de estudiante a inscribir
    while True:
            idEstudiante = int(input("\nIngrese el ID del estudiate que se va a inscribir: "))
            #Necesito encontrar para agarrar el primero dato de la tupla y compararla 
            if idEstudiante in estudiantes:
                #Mostrar estudiante aca con todos sus datos excepto el ID
                break
            else:
                print("\nNo hay ningún estudiante con ese ID, seleccione otra opción")

def cancelarInscripcionFolio():
    print("cancelar la inscripcion de un alumno mediante su folio")
    
def listadoInscripcionesTaller():
    print("listado de inscripciones en los talleres")