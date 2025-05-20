from datos import talleres,inscripcionesTupla
import inscripciones
import utilerias


def agregarTalleres():
  utilerias.limpiarPantalla()
  print("-"*51)
  print("Agregar un nuevo taller\n")
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
    utilerias.llamarMenu

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
    while True:
        idTaller = int(input("\nIngrese el ID del Taller (valor negativo para ir al Menú):"))

        if idTaller < 0:
          utilerias.llamarMenu()
        if idTaller in talleres:
          utilerias.mostrarTaller(idTaller)
          taller = talleres[idTaller]
          break
        else:
          print("\nNo hay ningún taller con ese ID, seleccione otra opción")
    print("Presione Enter si no desea actualizar nada")
    nuevoNombre = input("Nuevo nombre del taller: ")
    nuevaFecha = input("Nueva Fecha de inicio: ")
    nuevaHora = input("Nueva Hora de inicio: ")
    while True:
          try:
              nuevaDuracion = int(input("Nueva duración del taller en horas: "))
              break
          except ValueError:
              print("\nTipo de dato incorrecto, ingrese un número")
              continue
    nuevoLugar = input("Nueva Aula del taller: ")
    while True:
      try:
          nuevaCapacidad = int(input("Nueva capacidad de alumnos en el taller: "))
          break
      except ValueError:
          print("\nTipo de dato incorrecto, ingrese un número")
          continue
    while True:
      try:
          nuevoCosto = float(input("Nuevo Costo del taller: "))
          break
      except ValueError:
          print("\nTipo de dato incorrecto, ingrese un número")
          continue
    #Mostrar el taller con datos actualizados pero sin realmente actualizar todavia solo sera como un muestreo

    actualizar = input("¿Confirmar el registro? (S/N): ").upper()
    utilerias.validarSiNo(actualizar)
    if actualizar == "S":
      if nuevoNombre != "":
          taller['nombre'] = nuevoNombre
      if nuevaFecha != "":
          taller['fecha'] = nuevaFecha
      if nuevaHora != "":
          taller['hora'] = nuevaHora
      if nuevaDuracion != "":
          taller['duracion'] = int(nuevaDuracion)
      if nuevoLugar != "":
          taller['lugar'] = nuevoLugar
      if nuevaCapacidad != "":
          taller['capacidad'] = int(nuevaCapacidad)
      if nuevoCosto != "":
          taller['costo']=float(nuevoCosto)
      utilerias.ordenamientoTalleres(resp)

    if actualizar == "N":
      otroActualizar = input("¿Continuar con la actualización de otro Taller? (S/N): ").upper()
      utilerias.validarSiNo(otroActualizar)
      if otroActualizar == "S":
        actualizarTalleres(resp)
      if otroActualizar == "N":
        utilerias.llamarMenu()     
    otroActualizar = input("¿Continuar con la actualización de otro Taller? (S/N): ").upper()
    utilerias.validarSiNo(otroActualizar)
    if otroActualizar == "S":
       actualizarTalleres(resp)
    if otroActualizar == "N":
       utilerias.llamarMenu()
def mostrarListado(resp):
    utilerias.ordenamientoTalleres(resp)