from datos import talleres
import utilerias


def agregarTalleres():
  while True:
        try:
            idtaller = int(input("ID del Taller: "))
            break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
  if idtaller < 0:
     print("Tipo de ID invalido escoga otro valor")   
     agregarTalleres() 
  for id in talleres:
    if idtaller == id:
      print("Ya hay un taller con ese ID \npor favor seleccione otro número\n ")
      agregarTalleres()
      break
  nombreTaller = input("Nombre del Taller: ")
  fechaInicio = input ("Fecha de inicio del taller: ")
  turno = input ("Ingrese el turno AM/PM: ").upper()
  while turno != "AM" and turno != "PM":
    turno = input ("Tipo de turno invalido escoja entre AM o PM: ").upper()
  horaInicio = input ("Hora inicio del taller: ")
  horaCompleta = f"{horaInicio} {turno}"
  duracionTaller = input ("Duración del taller en horas: ")
  duracionHoras = f"{duracionTaller} horas"
  lugarTaller = input ("Aula del taller: ").upper()
  capEstudiantes = int(input("Cupo maximo de estudiantes: "))
  costoTaller = float(input("Costo del taller: "))
  #mostrar datos con formato aplicado antes de confirmacion
  print("\n---------------Datos Adicionales--------------------",
  "\nNombre del taller:",nombreTaller,
  "\nFecha:",fechaInicio,
  "\nHora de inicio:",horaCompleta,
  "\nDuración:",duracionHoras,
  "\nLugar:",lugarTaller,
  "\nCapacidad máxima:",capEstudiantes,
  "\nCosto:$",costoTaller ,
  )
  print("-"*53)
  respuestaAgregar = input("¿Confirmar el registro? (S/N): ").upper()
  utilerias.validarSiNo(respuestaAgregar)
  if respuestaAgregar == "N":
    agregarTalleres()
  elif respuestaAgregar == "S":
      talleres[idtaller] = {
      "nombre": nombreTaller,
      "fecha": fechaInicio,
      "hora": horaCompleta,
      "duracion": f"{duracionTaller} horas",
      "lugar": lugarTaller,
      "capacidad": capEstudiantes,
      "costo": costoTaller  
    }

  utilerias.ordenamientoTalleres(respuestaAgregar)
  respuestaAñadir = input("¿Quiere añadir otro taller?: ").upper()
  utilerias.validarSiNo(respuestaAñadir)
  if respuestaAñadir == "S":
    agregarTalleres()
  elif respuestaAñadir == "N":
    import menu
    menu.menu()

def actualizarTalleres():
  print("opcion para actualizar talleres")

def bajaTalleres():
  print("opcion para dar de baja talleres")
 
def mostrarListado(resp):
    utilerias.ordenamientoTalleres(resp)