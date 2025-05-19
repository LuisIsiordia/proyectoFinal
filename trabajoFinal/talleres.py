from datos import talleres,inscripcionesTupla
import inscripciones
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
     print("ID invalido escoga otro valor")   
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

def bajaTalleres(resp):
    utilerias.ordenamientoTalleres(resp)
    while True:
        try:
          idtaller = int(input("Ingrese el ID del Taller (valor negativo para ir al Menú): "))

          if idtaller < 0:
            import menu
            menu.menu()
          break
        except ValueError:
            print("Tipo de dato incorrecto, ingrese un número")
            continue
          
    if idtaller not in talleres:
      print("El taller que busca dar de baja no existe en el catalogo.\n")
      bajaTalleres(resp)
    if idtaller in talleres:
      utilerias.mostrarTaller(idtaller)
      eliminar = input("Confirmar baja del taller?: (S/N): ").upper()
      if eliminar == "S":
          if any(insc[3] == idtaller for insc in inscripcionesTupla):
            borrarInsc = input("Hay inscripciones a ese taller y requiere primero cancelar las inscripciones del taller,"
                              "\nantes de poder borrar el taller."
                              "\n¿Desea cancelar las inscripciones?"
                              "\nEn caso de que no, volvera al menu principal (S/N): ").upper()
            if borrarInsc == "S":
              inscripciones.cancelarInscripcionIDtaller(idtaller)
              eliminar = input("Inscripciones dadas de baja ¿Continuar baja de taller? (S/N): ").upper()
              if eliminar == "S":
                del talleres [idtaller]
                utilerias.llamarMenu()
              if eliminar == "N":
                utilerias.llamarMenu()
            if borrarInsc == "N":
                utilerias.llamarMenu()
          del talleres [idtaller]
          utilerias.llamarMenu()
      if eliminar == "N":
        bajaTalleres(resp)


def actualizarTalleres(resp):
    utilerias.ordenamientoTalleres(resp)
 
def mostrarListado(resp):
    utilerias.ordenamientoTalleres(resp)