"""
HECHO POR:
ROBERT STEWART TEAZE LEGLEU - 236224
LUIS ANTONIO ISIORDIA ALVAREZ - 216662

"""
import talleres
import estudiantes
import inscripciones
import utilerias
def menu():
 utilerias.limpiarPantalla()
 while True:
   print("-"*18,"MENU PRINCIPAL","-"*18)
   print("\n 1.Agregar un nuevo taller al catalogo\n",
         "2.Dar de baja un taller del catalogo\n",
         "3.Actualizar los datos de un taller\n",
         "4.Mostrar el listado de talleres en el catalogo\n",
         "5.Registrar una inscripción a un taller\n",
         "6.Cancelar una inscripción por folio\n",
         "7.Mostrar el listado de inscripciones por taller\n",
         "8.Mostrar los estudiantes vigentes\n",
         "9.Terminar operacion")
   print("-"*51)
   resp=input("Teclee su opción: ")

     
   if resp=='1':
        talleres.agregarTalleres()
   elif resp=='2':
        talleres.bajaTalleres()
   elif resp=='3':        
        talleres.actualizarTalleres()
   elif resp=='4':
        talleres.mostrarListado(resp)
   elif resp=='5':
        inscripciones.registroInscripcionTaller(resp)
   elif resp=='6':
        inscripciones.cancelarInscripcionFolio()
   elif resp=='7':
        inscripciones.listadoInscripcionesTaller()
   elif resp=='8':
        estudiantes.estudiantes()
   elif resp=='9':
        print("fin")
        break
   else:
         print("Opción inválida. Intenta de nuevo.")
         utilerias.llamarMenu()
            
   print("-"*50)

menu()
